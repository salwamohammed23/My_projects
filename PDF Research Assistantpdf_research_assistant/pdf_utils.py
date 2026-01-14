import pdfplumber

def extract_text_from_pdf(pdf_file):
    """استخراج النص من ملف PDF"""
    text = ""
    try:
        # التعامل مع مسار الملف سواء كان Gradio File أو string
        file_path = pdf_file.name if hasattr(pdf_file, 'name') else pdf_file
        
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
    except Exception as e:
        return f"Error: Could not extract text from PDF. {str(e)}"
    
    return text
