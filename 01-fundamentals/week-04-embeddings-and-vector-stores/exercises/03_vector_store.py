"""
W04 · Exercise 03 — Vector Stores (FAISS + Qdrant)

Goal:
- Store embeddings in FAISS.
- Query for nearest neighbors.
- Repeat with Qdrant.
"""

import numpy as np
import faiss
from openai import OpenAI
import os
from qdrant_client import QdrantClient
from qdrant_client.http import models

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_embedding(text: str, model: str = "text-embedding-3-small") -> np.ndarray:
    return np.array(client.embeddings.create(input=text, model=model).data[0].embedding)

# ---------- FAISS ----------
def faiss_demo(docs: list[str]):
    dim = len(get_embedding(docs[0]))
    index = faiss.IndexFlatL2(dim)

    embeddings = [get_embedding(d) for d in docs]
    index.add(np.array(embeddings))

    query = get_embedding("royalty")
    D, I = index.search(np.array([query]), k=3)

    print("\n[FAISS Results]")
    for idx, dist in zip(I[0], D[0]):
        print(f"{docs[idx]} | distance={dist:.3f}")

# ---------- Qdrant ----------
def qdrant_demo(docs: list[str]):
    # In-memory Qdrant (no Docker required). For Docker: QdrantClient(host="localhost", port=6333)
    qdrant = QdrantClient(":memory:")
    collection = "demo"

    dim = len(get_embedding(docs[0]))
    qdrant.recreate_collection(
        collection_name=collection,
        vectors_config=models.VectorParams(size=dim, distance=models.Distance.COSINE),
    )

    for i, doc in enumerate(docs):
        qdrant.upsert(
            collection_name=collection,
            points=[models.PointStruct(id=i, vector=get_embedding(doc).tolist(), payload={"text": doc})],
        )

    query = get_embedding("royalty").tolist()
    hits = qdrant.search(collection_name=collection, query_vector=query, limit=3)

    print("\n[Qdrant Results]")
    for h in hits:
        print(f"{h.payload['text']} | score={h.score:.3f}")

if __name__ == "__main__":
    documents = [
        "The king ruled the land.",
        "The queen was admired.",
        "Programming with Python is fun.",
        "Dogs are loyal pets.",
        "Cats enjoy sunny spots."
    ]

    faiss_demo(documents)
    qdrant_demo(documents)
