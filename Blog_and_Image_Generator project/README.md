# Blog_and_Image_Generator project

1. **Streamlit Setup**:
   - The app uses `streamlit` to create a simple interface for generating a blog post, divided into an introduction, body, and conclusion. It also generates relevant images to go along with the text.
   - A header is displayed with the title "Project 2 - Blog Post Generator" and a `text_input` field is used to accept the keyword for the blog post.

2. **Language Model Integration**:
   - The app uses OpenAI’s language model (via `langchain.chat_models.ChatOpenAI`) to generate different sections of the blog post (introduction, body, conclusion) based on the input keyword.
   - Each section (intro, body, conclusion) is prompted separately using a list of messages to guide the model on what to generate.

3. **Generating Blog Sections**:
   - The introduction, body, and conclusion are generated by interacting with the language model via `SystemMessage` and `HumanMessage` prompts. 
   - The language model is instructed to match the language of the blog post to the language of the keyword input.

4. **Generating Image Descriptions**:
   - After generating each part of the blog post, a second interaction with the language model is triggered to extract relevant image descriptions from the generated text.
   - These image descriptions are then used as input for a Hugging Face stable diffusion model to generate accompanying images.

5. **Hugging Face Image Generation**:
   - The app uses Hugging Face's `CompVis/stable-diffusion-v1-4` model to generate images based on the inferred image descriptions. 
   - A `requests.post()` call is made to Hugging Face's API, sending the image description as input, and retrieving the image as the output.
   - The image is then displayed alongside the corresponding section of the blog.

6. **Displaying Blog and Images**:
   - The blog content and images are displayed in columns. The introduction is paired with an image on the left, the body is displayed in full below, and the conclusion is paired with another image on the right.

### Example Flow

1. The user provides a keyword such as "Artificial Intelligence."
2. The app generates:
   - **Introduction**: A few sentences introducing the topic.
   - **Body**: A detailed section about the topic.
   - **Conclusion**: A summary or concluding paragraph.
3. The app also generates relevant images for the introduction and body sections, and displays them next to their respective content.

### Running the Application

To run this application:
1. Install the required libraries:
   ```bash
   pip install streamlit langchain openai requests pillow
   ```

2. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

The app will open in a browser, where users can enter a keyword and generate both blog content and relevant images.
