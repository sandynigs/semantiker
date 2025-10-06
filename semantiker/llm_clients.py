# semantiker/llm_clients.py
import requests
from .interfaces import BaseLLMClient

class OllamaClient(BaseLLMClient):
    """LLM client for the Ollama local service."""
    def __init__(self, api_url: str = "http://localhost:11434/api/generate"):
        self.api_url = api_url

    def generate(self, prompt: str, model: str = "mistral", max_tokens: int = 300, **kwargs) -> str:
        payload = {
            "model": model,
            "prompt": prompt,
            "options": {"num_predict": max_tokens}, # use num_predict for max_tokens in ollama
            "stream": False,
            **kwargs
        }

        try:
            response = requests.post(self.api_url, json=payload, timeout=120)
            response.raise_for_status()
            data = response.json()

            # Handle response structure
            if isinstance(data, dict) and "response" in data:
                return data["response"].strip()
            return str(data).strip()
        except requests.exceptions.RequestException as e:
            # Better error handling in a real package
            return f"Error querying Ollama: {e}"