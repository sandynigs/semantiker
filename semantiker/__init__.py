# semantiker/__init__.py

# Expose core components for easy access (makes 'from semantiker import X' work)
from .core import SemanticCacheUtility
from .llm_clients import OllamaClient
from .cache_backends import BaseCache  # Assuming this is a key interface
from .interfaces import BaseEmbedder   # Assuming this is a key interface

__all__ = [
    "SemanticCacheUtility",
    "OllamaClient",
    "BaseCache",
    "BaseEmbedder",
]