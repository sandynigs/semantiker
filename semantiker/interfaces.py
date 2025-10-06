from abc import ABC, abstractmethod
from typing import List, Tuple, Optional, Any

# --- Embedder Interface ---
class BaseEmbedder(ABC):
    """Abstract base class for all embedding models."""
    @abstractmethod
    def embed(self, text: str) -> 'np.ndarray':
        """
        Generates a normalized embedding vector for the given text.
        Returns a numpy array (float32, 1-D vector).
        """
        pass

    @property
    @abstractmethod
    def dim(self) -> int:
        """The dimension of the embedding vector."""
        pass

# --- Cache Interface ---
class BaseCache(ABC):
    """Abstract base class for all semantic cache storage backends."""
    @abstractmethod
    def store(self, embedding: 'np.ndarray', response: str) -> None:
        """
        Stores an embedding vector and its corresponding response.
        """
        pass

    @abstractmethod
    def lookup(self, embedding: 'np.ndarray', threshold: float) -> Optional[str]:
        """
        Searches for a similar embedding and returns the cached response
        if similarity is above the threshold.
        """
        pass

# --- LLM Client Interface ---
class BaseLLMClient(ABC):
    """Abstract base class for all LLM providers."""
    @abstractmethod
    def generate(self, prompt: str, **kwargs) -> str:
        """
        Sends a prompt to the LLM and returns the text response.
        """
        pass