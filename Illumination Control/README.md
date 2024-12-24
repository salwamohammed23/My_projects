إليك ترجمة محتوى ملف `README.md` إلى الإنجليزية:



```markdown
# Gamma Correction for Images

This project allows you to upload an image and apply gamma correction to it using an interactive **Streamlit** user interface. You can adjust the gamma value and see its effect on the image in real-time, and also download the modified image.

## How to Use

### 1. **Set Up the Environment**

To run this project, make sure you have **Python 3.x** installed. Then, create a virtual environment and install the required dependencies:

```bash
# Create a virtual environment (optional)
python -m venv venv

# Activate the virtual environment
# On Linux/Mac:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install the requirements
pip install -r requirements.txt
```

### 2. **Run the App**

After installing the required libraries, you can run the app using the following command:

```bash
streamlit run gamma_correction_app.py
```

Open your browser and go to the link that will appear (usually: `http://localhost:8501`).

### 3. **Interact with the App**

- **Upload an Image**: Upload a **JPG** or **PNG** image.
- **Select Gamma Value**: Use the slider to choose a gamma value between 0.1 and 3.0.
- **View the Modified Image**: You will see the image after gamma correction is applied.
- **Download the Modified Image**: You can download the modified image using the "Download the Modified Image" button.

## Requirements

- **Streamlit**: For creating the interactive user interface.
- **OpenCV**: For image processing.
- **NumPy**: For handling mathematical operations on arrays.
- **Pillow**: For handling image loading and saving.

### Install the dependencies via `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Running the App

1. Run the app using Streamlit:
   ```bash
   streamlit run gamma_correction_app.py
   ```

2. Open your browser and go to `http://localhost:8501`.
3. Upload an image, adjust the gamma values, and download the modified image.

## Example

### Before and After Gamma Correction

- **Original Image**:
  ![Original Image](images/original_image_example.jpg)

- **Gamma Corrected Image (Gamma=2.0)**:
  ![Gamma Corrected Image](images/gamma_corrected_image_example.jpg)

## Contributors

- [Contributor Name or Your Name Here]

## License

This project is licensed under the [MIT License](LICENSE).
```

### Explanation of the Translation:
1. **Project Description**: Briefly describes what the project does.
2. **How to Use**: Provides instructions on setting up the environment and running the app.
3. **Requirements**: Lists the libraries and dependencies required for the project.
4. **How to Run the App**: Explains how to run the app locally using **Streamlit**.
5. **Example**: Provides a section for before-and-after images of the gamma correction process.
6. **Contributors**: Space for listing contributors or your own name.
7. **License**: A section for the project license (e.g., MIT License).

If you need any further adjustments or additional details, feel free to ask! 😊
