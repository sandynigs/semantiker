from typing import Optional
from .interfaces import BaseCache, BaseEmbedder, BaseLLMClient
from .embedders import STransformerEmbedder
from .cache_backends import InMemoryCache

class SemanticCacheUtility:
    """
    The main utility class for managing semantic caching and LLM calls.
    It depends on abstract interfaces for flexibility.
    """
    def __init__(self,
                 embedder: BaseEmbedder = None,
                 cache_backend: BaseCache = None,
                 llm_client: BaseLLMClient = None,
                 similarity_threshold: float = 0.8):

        # Set default implementations if not provided
        self.embedder = embedder if embedder else STransformerEmbedder()
        # Cache backend needs the embedder's dimension
        self.cache = cache_backend if cache_backend else InMemoryCache(dim=self.embedder.dim)
        self.llm_client = llm_client

        self.threshold = similarity_threshold

    def _embed(self, query: str) -> 'np.ndarray':
        """Helper to call the pluggable embedder."""
        return self.embedder.embed(query)

    def lookup(self, query: str) -> Optional[str]:
        """Check the cache for a semantically similar response."""
        q_emb = self._embed(query)
        return self.cache.lookup(q_emb, self.threshold)

    def store(self, query: str, response: str) -> None:
        """Store a new query-response pair in the cache."""
        q_emb = self._embed(query)
        self.cache.store(q_emb, response)

    def ask(self, query: str, **llm_params) -> dict:
        """
        Main method to retrieve from cache or call the LLM and store the result.
        """
        cached_response = self.lookup(query)
        if cached_response:
            return {"source": "cache", "response": cached_response}

        if not self.llm_client:
             raise ValueError("LLM Client is not configured.")

        # Call the LLM (passes 'model', 'max_tokens', etc., via llm_params)
        llm_response = self.llm_client.generate(prompt=query, **llm_params)
        
        self.store(query, llm_response)

        return {"source": "llm", "response": llm_response}