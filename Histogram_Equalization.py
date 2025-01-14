import cv2
import numpy as np
import streamlit as st
from PIL import Image

# دالة لتطبيق Histogram Equalization على صورة ملونة
def histogram_equalization_color(image):
    # فصل القنوات (Red, Green, Blue)
    r_channel, g_channel, b_channel = cv2.split(image)

    # دالة تطبيق Histogram Equalization على قناة لونية
    def equalize_channel(channel):
        hist, bins = np.histogram(channel.flatten(), 256, [0, 256])
        cdf = hist.cumsum()
        cdf_normalized = cdf * 255 / cdf[-1]
        return np.interp(channel.flatten(), bins[:-1], cdf_normalized).reshape(channel.shape).astype(np.uint8)

    # تطبيق Histogram Equalization على كل قناة
    r_equalized = equalize_channel(r_channel)
    g_equalized = equalize_channel(g_channel)
    b_equalized = equalize_channel(b_channel)

    # دمج القنوات المعالجة
    return cv2.merge([r_equalized, g_equalized, b_equalized])

# عنوان التطبيق
st.title("Histogram Equalization for Colored Images")

# تحميل الصورة
uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # قراءة الصورة
    image = Image.open(uploaded_file)
    img_array = np.array(image)

    # عرض الصورة الأصلية
    st.subheader("Original Image")
    st.image(image, caption="Original Image", use_column_width=True)

    # التحقق من أن الصورة ملونة
    if len(img_array.shape) == 3 and img_array.shape[2] == 3:
        # تحويل الصورة من PIL إلى تنسيق OpenCV (RGB)
        img_rgb = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)

        # تطبيق Histogram Equalization
        equalized_img_rgb = histogram_equalization_color(img_rgb)

        # عرض الصورة بعد التحسين
        st.subheader("Image After Histogram Equalization")
        # تحويل الصورة المعالجة إلى تنسيق مناسب للعرض
        equalized_img_display = cv2.cvtColor(equalized_img_rgb, cv2.COLOR_BGR2RGB)
        st.image(equalized_img_display, caption="Equalized Image", use_column_width=True)
    else:
        st.warning("Please upload a valid color image.")
else:
    st.info("Upload a color image to get started.")
