```markdown
# ImageResizer Pro

**ImageResizer Pro** is a Streamlit-based tool for resizing images with ease. It provides a simple interface where users can upload an image, specify new dimensions, and view the resized output instantly. This tool is ideal for quick image resizing tasks for web use, digital design, or personal use.

## Features
- **Image Upload:** Supports JPG, JPEG, and PNG image formats.
- **Dimension Input:** Allows users to specify custom width and height.
- **Real-Time Resizing:** Resizes images in real time with a single click.
- **Streamlined UI:** A minimal, distraction-free interface with hidden headers and footers for a clean look.

## Technologies Used
- **Streamlit**: For creating the web-based interface.
- **OpenCV**: For image processing and resizing.
- **NumPy**: For handling image data.
- **Matplotlib**: For optional future image handling and visualization.

## How to Use
1. **Upload an Image**: Click "Upload an Image" to upload a JPG, JPEG, or PNG file.
2. **Enter New Dimensions**: Specify the desired width and height for the resized image.
3. **Resize**: Click the "Resize" button to view the resized image.
4. **View and Download**: View the resized image directly on the interface. Further download functionality can be added if needed.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ImageResizerPro.git
   ```
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   streamlit run app.py
   ```

## Example Usage

```python
# Run this command to launch the app
streamlit run app.py
```

Once the app is running, open the link provided in the console (e.g., `http://localhost:8501`) to use the tool in your web browser.

## Future Enhancements
- **Download Option**: Enable direct download of resized images.
- **Aspect Ratio Lock**: Option to maintain aspect ratio when resizing.
- **Additional Filters**: Provide options for different interpolation methods (e.g., NEAREST, AREA, LANCZOS).

## Contributing
Feel free to fork this repository and submit pull requests for new features or bug fixes.
