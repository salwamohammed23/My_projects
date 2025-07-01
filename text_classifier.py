import streamlit as st
import torch
import torch.nn as nn
import re

# ========== إعدادات النموذج ==========

# نفس تصميم الشبكة المستخدم سابقًا
class EmbeddingTextClassifier(nn.Module):
    def __init__(self, vocab_size, embed_dim, num_classes):
        super(EmbeddingTextClassifier, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embed_dim, padding_idx=0)
        self.fc1 = nn.Linear(embed_dim, 128)
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(0.3)
        self.fc2 = nn.Linear(128, num_classes)

    def forward(self, input_ids):
        x = self.embedding(input_ids)
        x = x.mean(dim=1)
        x = self.fc1(x)
        x = self.relu(x)
        x = self.dropout(x)
        x = self.fc2(x)
        return x

# ========== إعداد المفردات والتوكن ==========

def simple_tokenizer(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    return text.split()

def encode_text(text, vocab, max_len=50):
    tokens = simple_tokenizer(text)
    ids = [vocab.get(token, vocab["<UNK>"]) for token in tokens]
    ids = ids[:max_len] + [vocab["<PAD>"]] * (max_len - len(ids))
    return torch.tensor([ids], dtype=torch.long)

# ========== إعداد الفئات ==========

labels_list = [
    "Safe", "Violent Crimes", "Elections", "Sex-Related Crimes", "Unsafe",
    "Non-Violent Crimes", "Child Sexual Exploitation", "Unknown S-Type", "Suicide & Self-Harm"
]

# ========== تحميل النموذج والمفردات ==========

@st.cache_resource
def load_model_and_vocab():
    # تحميل المفردات (يفترض أنها محفوظة في ملف .pt أو dict)
    vocab = torch.load("model/vocab.pt")  # أو استخدم نسخة hardcoded
    
    model = EmbeddingTextClassifier(
        vocab_size=len(vocab),
        embed_dim=100,
        num_classes=len(labels_list)
    )
    model.load_state_dict(torch.load("model/simple_text_classifier.pt", map_location="cpu"))
    model.eval()
    return model, vocab

model, vocab = load_model_and_vocab()

# ========== واجهة Streamlit ==========

st.set_page_config(page_title="تصنيف المحتوى النصي", layout="centered")
st.title("🧠 تصنيف النصوص إلى فئات السلامة")
st.markdown("ادخل نصًا وسيقوم النموذج بتحديد الفئة المناسبة 👇")

user_input = st.text_area("📝 أدخل نصًا للتصنيف", height=150)

if st.button("🔍 صنف النص"):
    if not user_input.strip():
        st.warning("من فضلك أدخل نصًا قبل الضغط على زر التصنيف.")
    else:
        input_ids = encode_text(user_input, vocab)
        with torch.no_grad():
            output = model(input_ids)
            predicted_class = torch.argmax(output, dim=1).item()
            st.success(f"📌 الفئة المتوقعة: **{labels_list[predicted_class]}**")
