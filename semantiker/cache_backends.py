import faiss
import numpy as np
from typing import Optional, List
from .interfaces import BaseCache

class InMemoryCache(BaseCache):
    """
    In-memory semantic cache using FAISS for efficient similarity search.
    """
    def __init__(self, dim: int):
        # IndexFlatIP uses Inner Product (IP), which equals Cosine Similarity
        # if the input vectors are normalized (handled by the Embedder).
        self.index = faiss.IndexFlatIP(dim)
        self._responses: List[str] = []

    def store(self, embedding: np.ndarray, response: str) -> None:
        # FAISS expects a 2D array: (1, dim)
        self.index.add(np.array([embedding], dtype='float32'))
        self._responses.append(response)

    def lookup(self, embedding: np.ndarray, threshold: float) -> Optional[str]:
        if not self._responses:
            return None

        # FAISS expects a 2D array: (1, dim)
        q_emb = np.array([embedding], dtype='float32')
        D, I = self.index.search(q_emb, k=1)  # D=Distance (Similarity), I=Index

        # Cosine similarity: D[0][0] is the similarity of the nearest neighbor
        if D[0][0] >= threshold:
            return self._responses[I[0][0]]
        return None