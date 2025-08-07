

````markdown
# 🧠 LangGraph-Powered Python Code Assistant

A smart, interactive Python code assistant built with [LangGraph](https://github.com/langchain-ai/langgraph), [Gradio](https://gradio.app), [ChromaDB](https://www.trychroma.com/), and [Groq API](https://groq.com/). This notebook enables code execution, explanation, and debugging through a conversational interface enhanced by vector search and stateful graph reasoning.

---

## 🚀 Features

- ✅ **Conversational Python Assistant**
- 📦 **Semantic Code Search with ChromaDB**
- 🤖 **Stateful Reasoning using LangGraph**
- 🧠 **Embeddings via Sentence-Transformers**
- 🌐 **Gradio Web Interface**
- 🔐 **API Integration with Groq (LLM Provider)**

---

## 🛠️ Installation

You can run this notebook in **Google Colab** or locally.

### ✅ Requirements

```bash
pip install gradio pandas groq sentence-transformers chromadb langgraph
````

> If running locally, make sure you have Python 3.8+ and Jupyter Notebook installed.

---

## 🔐 Setup API Key

To use Groq models, you must set your API key.

### In Google Colab:

```python
from google.colab import userdata
api_key_coder = userdata.get('coder')
```

### Or locally:

```python
import os
api_key_coder = os.getenv("GROQ_API_KEY")
```

---

## 📁 Project Structure

```text
LangGraph_Powered_Python_Code_Assistant.ipynb   # Main notebook
README.md                                       # Project documentation
```

---

## 🧪 Example Use-Cases

* "Explain what this function does."
* "Fix this code snippet."
* "Search for examples of pandas merging."

---

## ⚠️ Notes

* This notebook uses experimental libraries like `langgraph`.
* It's meant for educational or prototyping purposes.
* Ensure safe input handling if enabling public access.

---

## 📜 License

MIT License. See `LICENSE` file if available.

---

## ✨ Credits

Built using:

* [LangGraph](https://github.com/langchain-ai/langgraph)
* [Gradio](https://gradio.app)
* [ChromaDB](https://www.trychroma.com/)
* [Groq](https://groq.com/)
* [Sentence-Transformers](https://www.sbert.net/)

```

