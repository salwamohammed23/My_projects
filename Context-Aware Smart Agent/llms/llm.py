from langchain.llms.base import LLM
from pydantic import PrivateAttr
from groq import Groq
from typing import Optional, List
from api.env import api_key_coder

# --- Setup api
#from google.colab import userdata
#api_key_coder =userdata.get('Chat_with_Your_Context')


# --- Setup LLM using Groq ---
class GroqLLM(LLM):
    model: str = "deepseek-r1-distill-llama-70b"
    temperature: float = 0.6
    top_p: float = 0.95
    max_tokens: int = 4096
    api_key: Optional[str] = api_key_coder

    _client: Groq = PrivateAttr()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._client = Groq(api_key=self.api_key)

    @property
    def _llm_type(self) -> str:
        return "groq-llm"

    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        response = self._client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=self.temperature,
            top_p=self.top_p,
            max_tokens=self.max_tokens,
            stop=stop,
            stream=False
        )
        return response.choices[0].message.content.strip()

# --- Activate LLM ---
llm = GroqLLM()
