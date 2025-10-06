import numpy as np
from sentence_transformers import SentenceTransformer
from .interfaces import BaseEmbedder

class STransformerEmbedder(BaseEmbedder):
    """Implementation using Sentence-Transformers (e.g., all-MiniLM-L6-v2)."""
    def __init__(self, model_name: str = 'all-MiniLM-L6-v2'):
        self._model = SentenceTransformer(model_name)
        # Assuming the model is loaded to determine the dimension
        self._dim = self._model.get_sentence_embedding_dimension()

    def embed(self, text: str) -> np.ndarray:
        # Generate embedding
        vec = self._model.encode(text)
        # Normalize to unit vector for cosine similarity (Inner Product = Cosine Similarity)
        vec = vec / np.linalg.norm(vec)
        # Return as a 1-D numpy array
        return vec.astype('float32')

    @property
    def dim(self) -> int:
        return self._dim