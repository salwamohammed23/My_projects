import requests
import time
from langchain.tools import Tool
from typing import Optional, Any

from env import api_key_WebSearch

# --- Web Search Tool ---
class WebSearchError(Exception):
    """Custom exception for web search failures"""
    pass

def web_search(query: str, max_retries: int = 3, timeout: int = 10) -> str:
    """
    Performs a web search using the Tavily API and returns the most relevant result.

    Args:
        query (str): The search query string
        max_retries (int): Maximum number of retry attempts (default: 3)
        timeout (int): Request timeout in seconds (default: 10)

    Returns:
        str: The content of the most relevant search result or an error message

    Raises:
        WebSearchError: If the search fails after all retry attempts

    Example:
        >>> result = web_search("latest AI research papers 2024")
        >>> print(result)
    """
    api_key = api_key_WebSearch  # Prefer environment variable

    if not api_key:
        raise WebSearchError("API key not configured for web search")

    headers = {
        "Authorization": api_key,
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    payload = {
        "query": query,
        "include_raw_content": True,
        "max_results": 3  # Get top 3 results for better context
    }

    last_error = None

    for attempt in range(max_retries):
        try:
            response = requests.post(
                "https://api.tavily.com/search",
                headers=headers,
                json=payload,
                timeout=timeout
            )

            response.raise_for_status()
            data = response.json()

            # Process results with multiple fallback options
            if not data.get("results"):
                return "No relevant results found."

            # Return concatenated content from top 3 results for better context
            contents = [r.get("content", "") for r in data["results"][:3] if r.get("content")]
            return "\n\n".join(contents) or "No readable content available."

        except requests.exceptions.RequestException as e:
            last_error = str(e)
            if attempt < max_retries - 1:
                time.sleep(1 * (attempt + 1))  # Exponential backoff
            continue

    raise WebSearchError(f"Web search failed after {max_retries} attempts. Last error: {last_error}")

WebSearchTool = Tool.from_function(
    func=web_search,
    name="WebSearch",
    description="""
    Powerful web search capability that:
    - Retrieves the most up-to-date information from the web
    - Returns summarized content from multiple sources
    - Handles complex queries with multiple retries
    Use when you need current information beyond your knowledge cutoff.
    """,
    handle_tool_error=True
)
