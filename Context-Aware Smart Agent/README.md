```markdown
# 🤖 Context-Aware Smart Agent

An intelligent agent system that understands and processes user queries with optional contextual information.
Built with LangChain, Groq API, and Gradio, this system can extract answers from provided context or perform web searches when needed.

## 🌐 Live Demo

Try the live demo on Hugging Face Spaces:  
[![Hugging Face Spaces](https://img.shields.io/badge/🤗%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/SalwaM/Context-Aware_Smart_Agent)

## ✨ Features

- **Contextual Understanding**: Process questions with additional context using the `||` separator
- **Intelligent Answer Extraction**: Attempt to extract answers directly from provided context
- **Web Search Integration**: Fall back to real-time web searches using Tavily API when context is insufficient
- **Multi-language Support**: Handles both Arabic and English queries seamlessly
- **User-Friendly Interface**: Clean Gradio web interface with interactive examples
- **Error Handling**: Robust error handling for API failures and malformed inputs

## 🏗️ Project Structure

```
context-aware-smart-agent/
├── main.py                 # Main application entry point
├── requirements.txt        # Python dependencies
├── prompts/
│   └── context_judge_prompt.txt  # Prompt template for context evaluation
├── agent/
│   └── agent_runner.py    # Agent initialization and execution logic
├── llms/
│   └── llm.py             # Groq LLM wrapper and configuration
├── tools/
│   ├── web_search_tool.py # Tavily API web search integration
│   ├── Context_Relevance_Splitter.py  # Context processing logic
│   └── context_presence_judge.py      # Context evaluation tool
├── ui/
│   └── gradio_ui.py       # Gradio interface configuration
├── api/
│   └── env.py             # API key management
└── README.md
```

## 🛠️ Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd context-aware-smart-agent
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
   - Create a `.env` file in the root directory
   - Add your API keys:
     ```
     WebSearch=your_tavily_api_key
     Chat_with_Your_Context=your_groq_api_key
     ```

## 🚀 Usage

### Running the Application

```bash
python main.py
```

The application will launch a Gradio web interface accessible in your browser.

### Input Format

Use the `||` separator to provide context with your question:

```
Question||Context
```

### Examples

- **Without context**: "What is the capital of France?"
- **With relevant context**: "العاصمة السعودية هي الرياض||ما هي عاصمة السعودية؟"
- **With irrelevant context**: "العاصمة السعودية هي الرياض||ما هي عاصمة مصر؟"
- **Context with different question**: "طقس القاهرة اليوم مشمس||ما هي عاصمة مصر؟"

## 🔧 Configuration

### API Requirements

1. **Groq API**: Required for LLM inference (deepseek-r1-distill-llama-70b model)
2. **Tavily API**: Required for web search functionality

### Model Settings

- **Model**: deepseek-r1-distill-llama-70b
- **Temperature**: 0.6 (balanced creativity and focus)
- **Top_p**: 0.95
- **Max Tokens**: 4096

### Search Settings

- **Max Results**: 3 top search results
- **Retry Attempts**: 3 with exponential backoff
- **Timeout**: 10 seconds per request

## 🎯 How It Works

### Processing Pipeline

1. **Input Reception**: User provides question with optional context
2. **Context Splitting**: System separates context from question using `||`
3. **Relevance Evaluation**: LLM judges if context is relevant to the question
4. **Answer Extraction**: Attempts to extract answer directly from context
5. **Fallback Mechanism**: If context is insufficient, performs web search
6. **Response Generation**: Returns appropriate answer or search results

### Example Workflows

**Successful Context Extraction**:
```
Input: "العاصمة السعودية هي الرياض||ما هي عاصمة السعودية؟"
Output: "العاصمة السعودية هي الرياض" (extracted from context)
```

**Web Search Fallback**:
```
Input: "العاصمة السعودية هي الرياض||ما هي عاصمة مصر؟"
Output: Web search results about Egypt's capital
```

## 🌐 API Integration

### Groq API
- Used for all LLM inference tasks
- Supports the deepseek-r1-distill-llama-70b model
- Handles context evaluation and answer extraction

### Tavily API
- Provides real-time web search capabilities
- Returns summarized content from multiple sources
- Includes automatic retry logic for reliability

## 🚨 Error Handling

The system includes comprehensive error handling for:
- API connectivity issues and timeouts
- Malformed input formats
- Context relevance failures
- Search result processing errors
- LLM response parsing issues

## 📊 Performance

- **Response Time**: Typically 2-10 seconds depending on query complexity
- **Accuracy**: High for context-relevant queries with proper formatting
- **Reliability**: Robust fallback mechanisms ensure responses in most scenarios

## 🔮 Future Enhancements

- [ ] Support for document upload and processing
- [ ] Conversation history and context persistence
- [ ] Additional search providers and APIs
- [ ] Customizable model parameters per user
- [ ] Export functionality for results and conversations
- [ ] Advanced context memory across sessions
- [ ] Multi-modal input support (images, documents)

## 📄 License

This project is available for educational and research purposes. Please ensure you comply with the terms of service for all integrated APIs.

## 🤝 Contributing

Contributions are welcome! Please feel free to:
- Submit bug reports and feature requests
- Create pull requests with improvements
- Add support for additional languages and models
- Enhance documentation and examples

## 📞 Support

For issues related to:
- **API keys**: Contact Groq and Tavily support
- **Code functionality**: Open an issue in the repository
- **Deployment problems**: Check the troubleshooting section

---

**Note**: This system requires valid API keys for Groq and Tavily services. Ensure you have proper subscriptions and rate limits configured before deployment.

**Live Demo**: Try the application on [Hugging Face Spaces](https://huggingface.co/spaces/SalwaM/Context-Aware_Smart_Agent)
```

I've added the Hugging Face Spaces link in two places:
1. In a dedicated "Live Demo" section at the top with a badge for better visibility
2. At the very bottom of the README for users who scroll all the way down

The badge format makes it visually appealing and clearly indicates that there's a live version available to try.
