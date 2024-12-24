import streamlit as st
import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# عنوان التطبيق
st.title("تطبيق تصحيح جاما (Gamma Correction)")

# وصف التطبيق
st.write("""
قم بتحميل صورة لمعاينة تأثير تصحيح جاما باستخدام قيم جاما مختلفة.
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

    # قيم معامل جاما
    gamma_values = [0.5, 1.0, 2.2]  # جاما 0.5 للتفتيح، 1.0 بدون تغيير، 2.2 للتغميق
    c = 1.0  # ثابت التحكم

    # تطبيق تصحيح جاما وعرض النتائج
    st.subheader("نتائج تصحيح جاما:")
    col1, col2, col3 = st.columns(3)  # تقسيم النتائج إلى ثلاثة أعمدة

    for idx, gamma in enumerate(gamma_values):
        # تطبيع الصورة إلى النطاق [0, 1]
        normalized_img = img_rgb / 255.0
        # تطبيق صيغة Power-Law Transformation: s = c * r^gamma
        gamma_corrected = c * (normalized_img ** gamma)
        # إعادة القيم إلى النطاق [0, 255] وتحويلها إلى نوع uint8
        gamma_corrected = np.uint8(np.clip(gamma_corrected * 255, 0, 255))

        # عرض الصورة المحولة
        if idx == 0:
            col1.image(gamma_corrected, caption=f"Gamma = {gamma}", use_column_width=True)
        elif idx == 1:
            col2.image(gamma_corrected, caption=f"Gamma = {gamma}", use_column_width=True)
        elif idx == 2:
            col3.image(gamma_corrected, caption=f"Gamma = {gamma}", use_column_width=True)
