import streamlit as st
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from peft import PeftModel
import torch
import zipfile
import os

# 1. إعداد المسارات
MODEL_ZIP = "toxic_classifier.zip"
EXTRACT_DIR = "./models"

# 2. فك الضغط (يتم مرة واحدة)
if not os.path.exists(EXTRACT_DIR):
    with zipfile.ZipFile(MODEL_ZIP, 'r') as zip_ref:
        zip_ref.extractall(EXTRACT_DIR)

# 3. تحميل النموذج
@st.cache_resource  # للتخزين المؤقت في Streamlit
def load_model():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    
    tokenizer = AutoTokenizer.from_pretrained(os.path.join(EXTRACT_DIR, "full_model"))
    
    model = AutoModelForSequenceClassification.from_pretrained(
        os.path.join(EXTRACT_DIR, "full_model"),
        device_map="auto"
    )
    return tokenizer, model

# 4. واجهة Streamlit
st.title("تصنيف النصوص السامة")
text_input = st.text_area("أدخل النص هنا:")

if st.button("صنّف"):
    if text_input:
        tokenizer, model = load_model()
        
        inputs = tokenizer(text_input, return_tensors="pt").to(model.device)
        with torch.no_grad():
            outputs = model(**inputs)
        
        probs = torch.nn.functional.softmax(outputs.logits, dim=1)[0]
        
        st.subheader("النتائج:")
        for i, prob in enumerate(probs):
            st.progress(float(prob), text=f"{model.config.id2label[i]}: {prob*100:.2f}%")
    else:
        st.warning("الرجاء إدخال نص أولاً")
