"""
W04 · Exercise 01 — Basic Embeddings

Goal:
- Generate embeddings using OpenAI.
- Compute cosine similarity manually.
"""

import os
import numpy as np
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_embedding(text: str, model: str = "text-embedding-3-small") -> list[float]:
    """Generate an embedding for the given text."""
    resp = client.embeddings.create(input=text, model=model)
    return resp.data[0].embedding

def cosine_similarity(vec1: list[float], vec2: list[float]) -> float:
    """Compute cosine similarity between two vectors."""
    v1, v2 = np.array(vec1), np.array(vec2)
    return float(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)))

if __name__ == "__main__":
    words = ["king", "queen", "man", "woman"]
    embeddings = {w: get_embedding(w) for w in words}

    sim = cosine_similarity(embeddings["king"], embeddings["queen"])
    print(f"Similarity king–queen: {sim:.3f}")

    # TODO: Print similarities for king–man, queen–woman, etc.
