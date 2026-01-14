from groq import Groq

# تمرير مفتاح API من Colab أو متغير البيئة
def init_groq(api_key):
    return Groq(api_key=api_key)

def generate_answer(groq_client, context, question):
    """إنشاء الرد على السؤال باستخدام Groq"""
    prompt = f"""You are a research assistant. Answer the question based ONLY on the provided context.

Context from the document:
{context}

Question: {question}

Instructions:
1. Answer based ONLY on the information in the context above.
2. If the context doesn't contain relevant information, say "The document doesn't contain information about this."
3. Be clear and concise.
4. Provide page references if available.
5. Use bullet points for lists when appropriate.
"""
    response = groq_client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.1,
        max_tokens=500
    )
    return response.choices[0].message.content
