# 01_reranking.py

"""
Task: Apply cross-encoder reranking to first-pass retrieved docs.
"""

from sentence_transformers import CrossEncoder

def rerank(query: str, candidates: list[str], top_k: int = 5):
    model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")
    pairs = [[query, doc] for doc in candidates]
    scores = model.predict(pairs)
    reranked = sorted(zip(candidates, scores), key=lambda x: x[1], reverse=True)
    return reranked[:top_k]


if __name__ == "__main__":
    query = "What are embeddings used for?"
    docs = [
        "Embeddings map text to vectors in high-dimensional space.",
        "They are used to store metadata in SQL databases.",
        "Vector similarity search enables semantic retrieval."
    ]
    results = rerank(query, docs, top_k=2)
    for doc, score in results:
        print(f"{score:.4f} :: {doc}")
