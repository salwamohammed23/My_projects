import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer

# تهيئة نموذج الـ embedding
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# تهيئة ChromaDB
client = chromadb.Client(Settings(
    persist_directory="rag_db",
    anonymized_telemetry=False
))

# الحصول على مجموعة (Collection)
def get_collection():
    return client.get_or_create_collection(
        name="pdf_collection",
        metadata={"hnsw:space": "cosine"}
    )

# مسح المجموعة القديمة
def clear_collection():
    try:
        client.delete_collection("pdf_collection")
    except:
        pass
    return client.create_collection(
        name="pdf_collection",
        metadata={"hnsw:space": "cosine"}
    )

# إضافة النصوص والـ embeddings إلى قاعدة البيانات
def add_to_collection(chunks):
    collection = get_collection()
    embeddings = embedding_model.encode(chunks).tolist()
    collection.add(
        documents=chunks,
        embeddings=embeddings,
        ids=[f"chunk_{i}" for i in range(len(chunks))]
    )

# البحث عن أجزاء النص الأكثر صلة بالسؤال
def query_collection(question, n_results=3):
    collection = get_collection()
    query_embedding = embedding_model.encode(question).tolist()
    docs = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )
    context = "\n".join(docs["documents"][0]) if docs["documents"] else ""
    return context
