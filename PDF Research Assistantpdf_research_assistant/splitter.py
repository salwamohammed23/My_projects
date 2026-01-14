from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_text_into_chunks(text, chunk_size=800, chunk_overlap=150):
    """تقسيم النص إلى أجزاء صغيرة للتخزين والبحث"""
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    chunks = splitter.split_text(text)
    return chunks
