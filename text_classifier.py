import streamlit as st
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences
import tensorflow as tf
import pickle

# تحميل النموذج والمعالج tokenizer
@st.cache_resource
def load_model_and_tokenizer():
    model = tf.keras.models.load_model("model/text_classifier_cnn.h5")  # تأكد من المسار الصحيح
    with open("model/tokenizer.pickle", "rb") as f:
        tokenizer = pickle.load(f)
    return model, tokenizer

# تعريف دالة التصنيف
def classify_text(text, model, tokenizer, id2label, max_length=100):
    sequence = tokenizer.texts_to_sequences([text])
    if not sequence[0]:  # إذا كان النص غير موجود في المفردات
        return {
            'text': text,
            'predicted_label': "Unknown",
            'predicted_id': -1,
            'probabilities': {"Unknown": 1.0}
        }
    padded = pad_sequences(sequence, maxlen=max_length, padding='post', truncating='post')
    prediction = model.predict(padded, verbose=0)
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
try:
    model, tokenizer = load_model_and_tokenizer()
except Exception as e:
    st.error(f"حدث خطأ في تحميل النموذج: {e}")
    st.stop()

# تعريف أسماء التصنيفات
class_names = [
    "Safe", "Violent Crimes", "Elections", "Sex-Related Crimes", "Unsafe",
    "Non-Violent Crimes", "Child Sexual Exploitation", "Unknown S-Type", "Suicide & Self-Harm"
]
id2label = {str(i): label for i, label in enumerate(class_names)}

# واجهة المستخدم
st.title("تطبيق تصنيف النصوص")
st.markdown("أدخل نصًا ليتم تصنيفه بواسطة النموذج المدرب")

# إدخال المستخدم
user_input = st.text_area("📝 أدخل النص هنا", height=150, help="اكتب النص الذي تريد تصنيفه")

# زر التصنيف
if st.button("🔍 تصنيف", type="primary"):
    if not user_input.strip():
        st.warning("⚠️ يرجى إدخال نص للتصنيف.")
    else:
        with st.spinner("جاري معالجة النص..."):
            try:
                result = classify_text(user_input, model, tokenizer, id2label)
                
                st.subheader("🔎 النتائج:")
                st.write(f"**النص المدخل:** {result['text']}")
                
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("التصنيف المتوقع", result['predicted_label'])
                with col2:
                    st.metric("معرف التصنيف", result['predicted_id'])
                
                st.subheader("📊 توزيع الاحتمالات:")
                st.bar_chart(result["probabilities"])
                
                # عرض الاحتمالات كجدول
                st.subheader("📋 تفاصيل الاحتمالات:")
                prob_data = [(label, f"{prob:.4f}") for label, prob in result["probabilities"].items()]
                st.table(prob_data)
                
            except Exception as e:
                st.error(f"حدث خطأ أثناء التصنيف: {e}")

# تذييل الصفحة
st.markdown("---")
st.caption("تطبيق تصنيف النصوص - تم التطوير باستخدام TensorFlow و Streamlit")
