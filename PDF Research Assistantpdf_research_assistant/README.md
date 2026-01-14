
# **📚 PDF Research Assistant – Research Tool**

### **Live Demo:**

Try it online: [Hugging Face Demo](https://huggingface.co/spaces/SalwaM/PDF_Research_Assistant)

---

### **Project Description**

The **PDF Research Assistant** is an interactive tool that allows users to upload PDF files and ask questions about their content. The system extracts text from PDFs, splits it into semantic chunks, and generates embeddings for efficient retrieval. Answers are provided using a **Groq large language model (LLM)**, based solely on the context of the document.

This tool supports **both English and Arabic interfaces**, making it accessible for a wide audience.

---

### **Key Features**

* **Text Extraction:** Extracts text from PDF files (supports most text-based PDFs).
* **Chunking & Semantic Search:** Splits text into meaningful chunks and stores them in **ChromaDB** for efficient retrieval.
* **Contextual Question Answering:** Uses **Groq LLM** to answer questions strictly based on the document content.
* **Dual Language Interface:** Supports English and Arabic for wider accessibility.
* **Interactive Demo:** Fully functional web interface via **Gradio**, accessible online.

---

### **Technologies & Tools**

* **Python** – Core programming language
* **Gradio** – Interactive web interface
* **ChromaDB** – Embedding-based document store
* **SentenceTransformers** – Text embeddings
* **Groq API** – LLM for generating answers
* **pdfplumber** – Extract text from PDFs
* **Langchain Text Splitters** – Chunking large text

---

### **Skills Highlighted**

* **NLP & RAG (Retrieval-Augmented Generation)**
* Embeddings creation and semantic search
* LLM integration for contextual Q&A
* Interactive web interface development
* Modular project design and clean architecture

---

### **Example Workflow**

1. **Upload PDF** – User uploads a PDF file.
2. **Ask a Question** – Type a question about the PDF’s content.
3. **Retrieve Context** – System searches for relevant chunks from the document.
4. **Generate Answer** – Groq LLM provides a clear, concise answer.

---

### **Example Question & Answer**

* **Question:** What is the main idea of this document?
* **Answer:** The system extracts relevant text and summarizes the key idea, providing bullet points or page references if available.

*(Add a GIF or screenshot here showing the workflow in action from your Hugging Face demo.)*

---

### **Why This Project Stands Out**

* Real, **interactive demo online**, proving the project works.
* Modular architecture makes it easy to expand with new features (e.g., DOCX support, translation, additional languages).
* Demonstrates **full-stack AI capability**, from data preprocessing to LLM-powered insights.
* Shows expertise in **state-of-the-art AI tools** like ChromaDB, Groq LLM, and SentenceTransformers.

---


