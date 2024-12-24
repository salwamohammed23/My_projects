import streamlit as st
import cv2
import numpy as np
from PIL import Image
import io
# Add custom CSS to hide the footer, header
hide_st_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)
# إعداد واجهة المستخدم

# عنوان التطبيق
st.title("تطبيق تصحيح جاما (Gamma Correction)")

# وصف التطبيق
st.write("""
قم بتحميل صورة واستخدم مؤشر التحكم لاختيار قيمة جاما ومعاينة النتائج، 
ثم قم بتحميل الصورة المعدلة.
""")

# رفع الصورة
uploaded_file = st.file_uploader("قم برفع صورة", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # قراءة الصورة باستخدام PIL
    image = Image.open(uploaded_file)
    img_rgb = np.array(image)  # تحويل الصورة إلى مصفوفة NumPy

    # عرض الصورة الأصلية
    st.subheader("الصورة الأصلية:")
    st.image(img_rgb, caption="الصورة الأصلية", use_container_width=True)

    # شريط تمرير لاختيار قيمة جاما
    gamma = st.slider("اختر قيمة جاما", min_value=0.1, max_value=3.0, value=1.0, step=0.1)

    # تطبيق تصحيح جاما
    c = 1.0  # ثابت التحكم
    normalized_img = img_rgb / 255.0  # تطبيع الصورة إلى النطاق [0, 1]
    gamma_corrected = c * (normalized_img ** gamma)  # تطبيق تصحيح جاما
    gamma_corrected = np.uint8(np.clip(gamma_corrected * 255, 0, 255))  # إعادة القيم إلى النطاق [0, 255]

    # عرض الصورة المحولة
    st.subheader("الصورة بعد تصحيح جاما:")
    st.image(gamma_corrected, caption=f"Gamma = {gamma}", use_container_width=True)

    # تحويل الصورة المعدلة إلى صيغة يمكن تحميلها (BytesIO)
    img_pil = Image.fromarray(gamma_corrected)
    img_byte_arr = io.BytesIO()
    img_pil.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)

    # زر تحميل الصورة المعدلة
    st.download_button(
        label="تحميل الصورة المعدلة",
        data=img_byte_arr,
        file_name="gamma_corrected_image.png",
        mime="image/png"
    )
