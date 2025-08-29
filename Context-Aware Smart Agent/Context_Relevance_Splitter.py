from typing import Union, Dict
from langchain.tools import Tool

from llm import llm

# --- Enhanced Context Processing Tool ---
def Context_Relevance_Splitter(input_text: str) -> Union[str, Dict[str, str]]:
    """
    Advanced context processing with improved error handling and answer extraction.
    """
    try:
        # If there is no context (no ||)
        if "||" not in input_text:
            return {
                "core_question": input_text.strip(),
                "background": "",
                "answer_found": False,
                "query_for_search": input_text.strip()
            }

        # Split context from question
        parts = [p.strip() for p in input_text.split("||", 1) if p.strip()]

        # Check if there are two parts (context and question)
        if len(parts) < 2:
            return "⚠ Please use the format: question||context"

        context, question = parts[0], parts[1]

        # Check context relevance
        relevance_prompt = f"""
        Is the following context relevant to the question?
        Context: {context}
        Question: {question}

        Answer only with yes or no:
        """

        relevance_response = llm(relevance_prompt).strip().lower()

        if "yes" not in relevance_response and "نعم" not in relevance_response:
            return {
                "background": context,
                "core_question": question,
                "answer_found": False,
                "query_for_search": question,
                "message": "🚫 Irrelevant context - will search for answer externally"
            }

        # Try to extract answer from context
        answer_extraction_prompt = f"""
        Based on the following context, answer the question.
        If the answer is not found in the context, say "ANSWER_NOT_FOUND".

        Context: {context}
        Question: {question}

        Answer:
        """

        answer_response = llm(answer_extraction_prompt).strip()

        # Check if answer was found in context
        if "ANSWER_NOT_FOUND" in answer_response.upper():
            return {
                "background": context,
                "core_question": question,
                "answer_found": False,
                "query_for_search": question,
                "extracted_answer": None,
                "message": "Answer not found in context - requires external search"
            }
        else:
            return {
                "background": context,
                "core_question": question,
                "answer_found": True,
                "query_for_search": None,
                "extracted_answer": answer_response,
                "message": "Answer successfully extracted from context"
            }

    except Exception as e:
        # In case of any unexpected error
        return {
            "core_question": input_text.strip(),
            "background": "",
            "answer_found": False,
            "query_for_search": input_text.strip(),
            "error": str(e)
        }

# --- Agent Tool Definition ---
Context_Relevance_Splitter_tool = Tool.from_function(
    func=Context_Relevance_Splitter,
    name="ContextProcessor",
    description="""
    Advanced context processing and answer extraction tool:
    1. Checks relevance of context to the question
    2. Attempts to extract answer from context
    3. If answer not found, returns query for external search
    4. Splits context from the core question
    Use format: question||context
    Returns: answer_found, extracted_answer, query_for_search
    """
)
