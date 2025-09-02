# 03_context_building.py

"""
Task: Build context with ordering, source tags, and citations.
"""

def build_context(passages: list[str]):
    context, citations = [], {}
    for i, p in enumerate(passages, start=1):
        tag = f"[S{i}]"
        context.append(f"{tag} {p}")
        citations[tag] = p
    return "\n".join(context), citations


if __name__ == "__main__":
    docs = [
        "Embeddings are vector representations of text.",
        "Cosine similarity is often used to compare embeddings.",
    ]
    ctx, cits = build_context(docs)
    print("Context:\n", ctx)
    print("Citations:", cits)
