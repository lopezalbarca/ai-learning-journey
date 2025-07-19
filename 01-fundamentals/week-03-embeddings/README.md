# Fundamentals - 03 - Embeddings Deep Dive

## 🧠 Goal

This week is dedicated to understanding embeddings in depth: how they work, how to generate them, and how to store and query them efficiently using vector databases.

By the end of the week, I aim to:
- Understand the theory behind embeddings (cosine similarity, vector space)
- Compare different embedding models (OpenAI vs open-source)
- Explore vector DBs in more detail (Qdrant, Chroma, Pinecone)
- Evaluate chunking strategies and indexing performance

---

## 📚 Resources Used (to be filled)

| Resource | Type |
|----------|------|
| [OpenAI Embeddings Docs](https://platform.openai.com/docs/guides/embeddings) | Official guide |
| Qdrant / Chroma / Weaviate / Pinecone docs | Vector DBs |
| YouTube: “Embeddings 101” by Pinecone / Data School | Video |
| Notebooks: LangChain / LlamaIndex examples | Code examples |

---

## 📦 Folder Contents

| File / Folder | Description |
|---------------|-------------|
| `README.md` | Weekly summary (this file) |
| `experiments/` | Tests with different models and chunking |
| `benchmarks.md` | Comparison results (recall, speed, etc.) |
| `utils/` | Helper scripts for indexing/querying |
| `notes.md` | Notes and ideas |

---

## ✅ Progress Log

- [ ] Generated embeddings with different models
- [ ] Compared cosine vs dot-product vs other similarities
- [ ] Tested chunk sizes and overlap strategies
- [ ] Benchmarked Qdrant vs Chroma with the same data

---

## 💡 Notes / Learnings

> - Smaller chunk sizes aren’t always better for recall  
> - Indexing strategy can greatly affect latency  
> - Visualizing embeddings (e.g., with UMAP or t-SNE) is helpful to understand clusters

---

**Next steps:** Use all insights from embeddings to build a full RAG pipeline for real use cases (see Week 4).