import gradio as gr
from pdf_utils import extract_text_from_pdf
from splitter import split_text_into_chunks
from embedding_db import add_to_collection, clear_collection, query_collection
from groq_client import init_groq, generate_answer
from google.colab import userdata

# تهيئة Groq
api_key_coder = userdata.get('coder')
groq_client = init_groq(api_key_coder)

def answer_from_pdf(pdf_file, question):
    """دالة معالجة PDF والإجابة على السؤال"""
    if pdf_file is None:
        return "⚠️ Please upload a PDF file first."
    if not question.strip():
        return "⚠️ Please enter a question."
    
    # مسح المجموعة القديمة
    clear_collection()
    
    # استخراج النص
    text = extract_text_from_pdf(pdf_file)
    if text.startswith("Error:") or len(text.strip()) == 0:
        return text or "⚠️ Could not extract any text from the PDF."
    
    # تقسيم النص وإضافة إلى DB
    chunks = split_text_into_chunks(text)
    add_to_collection(chunks)
    
    # استرجاع السياق
    context = query_collection(question)
    
    # توليد الإجابة
    answer = generate_answer(groq_client, context, question)
    return answer

# واجهة Gradio
def create_interface():
    examples = [
        [None, "What is the main idea of this document?"],
        [None, "Summarize the content briefly."],
        [None, "What methodology is used in this paper?"]
    ]
    
    interface_en = gr.Interface(
        fn=answer_from_pdf,
        inputs=[gr.File(label="📄 Upload PDF", file_types=[".pdf"], type="filepath"),
                gr.Textbox(label="❓ Question", lines=2, placeholder="Type your question here...")],
        outputs=gr.Textbox(label="✅ Answer", lines=10),
        title="📚 PDF Research Assistant",
        examples=examples,
        theme=gr.themes.Soft()
    )
    
    interface_ar = gr.Interface(
        fn=answer_from_pdf,
        inputs=[gr.File(label="📄 ارفع ملف PDF", file_types=[".pdf"], type="filepath"),
                gr.Textbox(label="❓ السؤال", lines=2, placeholder="اكتب سؤالك هنا...")],
        outputs=gr.Textbox(label="✅ الإجابة", lines=10),
        title="📚 مساعد البحث في ملفات PDF",
        examples=examples,
        theme=gr.themes.Soft()
    )
    
    demo = gr.TabbedInterface([interface_en, interface_ar], ["English Version", "النسخة العربية"])
    return demo
