# Smart_Code_Evaluator

1. **Streamlit Setup**:
   - The app uses the `streamlit` library to create a simple user interface with text input fields for a task description and code solution. A button triggers the evaluation of the code.
   - The header displays "project_3", followed by two input fields: one for task description and another for code (solution).

2. **LangChain Integration**:
   - `OpenAI` and `ChatOpenAI` from the `langchain` library are used to interact with OpenAI's GPT models.
   - Your OpenAI API key is set up as `open_ai_key`, which allows the application to invoke language model responses.

3. **User Inputs**:
   - Users input a task description and the corresponding code solution they want to evaluate.
   - The `Generate` button triggers the evaluation process.

4. **Evaluation Criteria**:
   The app evaluates the code using five different aspects, each evaluated through a separate language model interaction:
   
   1. **Task Description Matching**:
      - Compares the task description with the submitted code to check if the code satisfies the task requirements.
      - Uses `SystemMessage` to set the prompt context, and the evaluation is performed using `chat.invoke`.
   
   2. **Modularity**:
      - Checks if the code follows good modularity practices (e.g., breaking it into functions, classes).
   
   3. **Efficiency and Readability**:
      - Evaluates the performance, cleanliness, and readability of the code.
   
   4. **Main Concepts Inclusion**:
      - Checks whether key programming concepts like preprocessing, data splitting, training, and testing are present.
   
   5. **AI-Generated Code Detection**:
      - Analyzes the code to judge whether it was likely AI-generated or written manually.

5. **Displaying Results**:
   - After generating responses from the language model for each of the five categories, the results are displayed using `st.write` under appropriate subheaders.

### Running the Application

To run the application:
1. Install the required libraries:

```bash
pip install streamlit langchain openai
```

2. Run the Streamlit app using:

```bash
streamlit run app.py
```

The app will open in your web browser, where you can input the task description and code, then get feedback on various aspects of the cod
