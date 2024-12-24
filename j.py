import streamlit as st
import cv2
import numpy as np
from PIL import Image

# عنوان التطبيق
st.title("تطبيق تصحيح جاما (Gamma Correction)")

# وصف التطبيق
st.write("""
قم بتحميل صورة واستخدم مؤشر التحكم لاختيار قيمة جاما ومعاينة النتائج.
""")

# رفع الصورة
uploaded_file = st.file_uploader("قم برفع صورة", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # قراءة الصورة باستخدام PIL
    image = Image.open(uploaded_file)
    img_rgb = np.array(image)  # تحويل الصورة إلى مصفوفة NumPy

    # عرض الصورة الأصلية
    st.subheader("الصورة الأصلية:")
    st.image(img_rgb, caption="الصورة الأصلية", use_column_width=True)

    # شريط تمرير لاختيار قيمة جاما
    gamma = st.slider("اختر قيمة جاما", min_value=0.1, max_value=3.0, value=1.0, step=0.1)

    # تطبيق تصحيح جاما
    c = 1.0  # ثابت التحكم
    normalized_img = img_rgb / 255.0  # تطبيع الصورة إلى النطاق [0, 1]
    gamma_corrected = c * (normalized_img ** gamma)  # تطبيق تصحيح جاما
    gamma_corrected = np.uint8(np.clip(gamma_corrected * 255, 0, 255))  # إعادة القيم إلى النطاق [0, 255]

    # عرض الصورة المحولة
    st.subheader("الصورة بعد تصحيح جاما:")
    st.image(gamma_corrected, caption=f"Gamma = {gamma}", use_column_width=True)
