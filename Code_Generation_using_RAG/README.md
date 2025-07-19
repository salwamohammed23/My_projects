```markdown
# Code Generation using RAG

This project demonstrates a Retrieval-Augmented Generation (RAG) system for generating Python code using the Groq API and ChromaDB. The system retrieves similar code examples from a dataset and uses them as context to generate high-quality code snippets.

## Features

- **Embedding Generation**: Uses `all-MiniLM-L6-v2` to create vector representations of code prompts.
- **Vector Storage**: Stores code examples and their embeddings in ChromaDB for efficient retrieval.
- **Code Generation**: Leverages the Groq API (`deepseek-r1-distill-llama-70b`) to generate Python code based on user prompts and retrieved examples.
- **Context-Aware**: Retrieves similar examples to guide the generation process.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install the required dependencies:
   ```bash
   pip install groq sentence-transformers chromadb pandas
   ```

3. Set up your Groq API key:
   - Obtain an API key from [Groq](https://groq.com/).
   - Store the key securely (e.g., in Google Colab's user data or an environment variable).

## Usage

1. **Load the Dataset**:
   The system uses the `openai_humaneval` dataset from Hugging Face, which contains programming tasks and their solutions.

2. **Initialize Components**:
   ```python
   embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
   groq_client = Groq(api_key="your-api-key")
   client = chromadb.Client(Settings(anonymized_telemetry=False, persist_directory="rag_db"))
   collection = client.get_or_create_collection(name="code_examples", metadata={"hnsw:space": "cosine"})
   ```

3. **Add Examples to ChromaDB**:
   ```python
   def add_example(prompt, code):
       embedding = embedding_model.encode([prompt.strip()])[0]
       doc_id = hashlib.md5(prompt.encode()).hexdigest()
       collection.add(
           documents=[code.strip()],
           metadatas=[{"prompt": prompt, "type": "code_example"}],
           ids=[doc_id],
           embeddings=[embedding]
       )
   ```

4. **Retrieve Similar Examples**:
   ```python
   def retrieve_similar(prompt, top_k=2):
       embedding = embedding_model.encode([prompt])[0]
       results = collection.query(query_embeddings=[embedding], n_results=top_k)
       return results['documents'][0] if results['documents'] else None
   ```

5. **Generate Code**:
   ```python
   def generate_code_with_groq(prompt, context=None):
       messages = [{"role": "system", "content": "You are a helpful programming assistant that generates high-quality Python code, show code only idont want explan"}]
       if context:
           messages.append({"role": "system", "content": f"Here are some similar examples:\n{context}"})
       messages.append({"role": "user", "content": prompt})
       completion = groq_client.chat.completions.create(
           model="deepseek-r1-distill-llama-70b",
           messages=messages,
           temperature=0.7,
           max_tokens=2048,
       )
       return completion.choices[0].message.content
   ```

6. **Run the System**:
   ```python
   user_prompt = "write code to sum 9, 8"
   similar_examples = retrieve_similar(user_prompt)
   generated_code = generate_code_with_groq(user_prompt, "\n".join(similar_examples) if similar_examples else None)
   print(generated_code)
   ```

## Example Output

For the prompt `"write code to sum 9, 8"`, the system generates:
```python
sum(x for x in (9,8))
```

## Requirements

- Python 3.11+
- Libraries: `groq`, `sentence-transformers`, `chromadb`, `pandas`



## Acknowledgments

- Dataset: [OpenAI HumanEval](https://huggingface.co/datasets/openai/openai_humaneval)
- Embeddings: [SentenceTransformers](https://www.sbert.net/)
- Vector Database: [ChromaDB](https://www.trychroma.com/)
- API: [Groq](https://groq.com/)
```
