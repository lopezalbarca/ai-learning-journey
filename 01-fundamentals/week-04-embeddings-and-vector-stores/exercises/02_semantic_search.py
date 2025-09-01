"""
W04 · Exercise 02 — Semantic Search in Memory

Goal:
- Embed a set of documents.
- Query with cosine similarity to return top-k matches.
"""

import numpy as np
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_embedding(text: str, model: str = "text-embedding-3-small") -> list[float]:
    return client.embeddings.create(input=text, model=model).data[0].embedding

def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))

def search(query: str, embeddings: dict[str, np.ndarray], top_k: int = 3):
    q_emb = np.array(get_embedding(query))
    scores = [(doc, cosine_similarity(q_emb, emb)) for doc, emb in embeddings.items()]
    return sorted(scores, key=lambda x: x[1], reverse=True)[:top_k]

if __name__ == "__main__":
    documents = [
        "The cat sat on the mat.",
        "Dogs are loyal animals.",
        "The king ruled the kingdom.",
        "Queens are powerful leaders.",
        "I love programming in Python."
    ]

    doc_embeddings = {doc: np.array(get_embedding(doc)) for doc in documents}

    results = search("Who is a leader?", doc_embeddings, top_k=3)
    for doc, score in results:
        print(f"{score:.3f} | {doc}")
