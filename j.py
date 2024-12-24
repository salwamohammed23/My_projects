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


# App title
st.title("Illumination Control App")

# App description
st.write("""
Upload an image and use the control slider to select a gamma value and preview the results, 
then download the modified image.
""")

# Upload image
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Read the image using PIL
    image = Image.open(uploaded_file)
    img_rgb = np.array(image)  # Convert the image to a NumPy array

    # Display the original image
    st.subheader("Original Image:")
    st.image(img_rgb, caption="Original Image", use_container_width=True)

    # Slider to select the gamma value
    gamma = st.slider("Select Gamma Value", min_value=0.1, max_value=3.0, value=1.0, step=0.1)

    # Apply gamma correction
    c = 1.0  # Control constant
    normalized_img = img_rgb / 255.0  # Normalize the image to the range [0, 1]
    gamma_corrected = c * (normalized_img ** gamma)  # Apply gamma correction
    gamma_corrected = np.uint8(np.clip(gamma_corrected * 255, 0, 255))  # Rescale back to [0, 255]

    # Display the gamma-corrected image
    st.subheader("Image After Gamma Correction:")
    st.image(gamma_corrected, caption=f"Gamma = {gamma}", use_container_width=True)

    # Convert the modified image to a format that can be downloaded (BytesIO)
    img_pil = Image.fromarray(gamma_corrected)
    img_byte_arr = io.BytesIO()
    img_pil.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)

    # Download button for the modified image
    st.download_button(
        label="Download Modified Image",
        data=img_byte_arr,
        file_name="gamma_corrected_image.png",
        mime="image/png"
    )
