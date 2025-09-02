# 02_passage_fusion.py

"""
Task: Merge complementary passages into a compact fused context.
"""

def fuse_passages(passages: list[str], max_chars: int = 500) -> str:
    # Deduplicate
    seen, fused = set(), []
    for p in passages:
        if p not in seen:
            seen.add(p)
            fused.append(p.strip())
    context = " ".join(fused)
    return context[:max_chars]


if __name__ == "__main__":
    passages = [
        "Embeddings represent semantic meaning of text.",
        "Semantic similarity is computed with cosine similarity.",
        "Embeddings represent semantic meaning of text."  # duplicate
    ]
    fused = fuse_passages(passages)
    print("Fused context:", fused)
