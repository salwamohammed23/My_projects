import streamlit as st
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences
import tensorflow as tf
import pickle

# تحميل النموذج والمعالج tokenizer
@st.cache_resource
def load_model_and_tokenizer():
    model = tf.keras.models.load_model("model/text_classifier_cnn.h5")  # غيّر هذا حسب اسم ملف النموذج
    with open("model/tokenizer.pickle", "rb") as f:
        tokenizer = pickle.load(f)
    return model, tokenizer

# تعريف دالة التصنيف
def classify_text(text, model, tokenizer, id2label, max_length=100):
    sequence = tokenizer.texts_to_sequences([text])
    padded = pad_sequences(sequence, maxlen=max_length, padding='post', truncating='post')
    prediction = model.predict(padded)
    predicted_id = int(np.argmax(prediction))
    predicted_label = id2label.get(str(predicted_id), f"class_{predicted_id}")
    probabilities = {
        id2label.get(str(i), f"class_{i}"): float(prob)
        for i, prob in enumerate(prediction[0])
    }
    return {
        'text': text,
        'predicted_label': predicted_label,
        'predicted_id': predicted_id,
        'probabilities': probabilities
    }

# تحميل النموذج والمعالج
model, tokenizer = load_model_and_tokenizer()

# تعريف أسماء التصنيفات
class_names = [
    "Safe", "Violent Crimes", "Elections", "Sex-Related Crimes", "Unsafe",
    "Non-Violent Crimes", "Child Sexual Exploitation", "Unknown S-Type", "Suicide & Self-Harm"
]
id2label = {str(i): label for i, label in enumerate(class_names)}

# واجهة المستخدم
st.title("Text Classification App")
st.markdown("أدخل نصًا ليتم تصنيفه بواسطة النموذج المدرب")

# إدخال المستخدم
user_input = st.text_area("📝 أدخل النص هنا", height=150)

# زر التصنيف
if st.button("🔍 تصنيف"):
    if user_input.strip() == "":
        st.warning("يرجى إدخال نص للتصنيف.")
    else:
        result = classify_text(user_input, model, tokenizer, id2label)
        st.subheader("🔎 النتيجة:")
        st.write(f"**النص:** {result['text']}")
        st.write(f"**التصنيف المتوقع:** {result['predicted_label']} (ID: {result['predicted_id']})")

        st.subheader("📊 احتمالات التصنيف:")
        st.bar_chart(result["probabilities"])
