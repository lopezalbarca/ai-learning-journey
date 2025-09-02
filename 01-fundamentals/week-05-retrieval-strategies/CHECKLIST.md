# W05 · Checklist

### Setup
- [ ] Virtual environment created and activated.
- [ ] Dependencies installed (`numpy`, `openai`, `faiss-cpu`, `qdrant-client`, `rank-bm25`).
- [ ] `env/requirements.txt` generated and committed.

### Chunking
- [ ] Implemented fixed-size chunking.
- [ ] Implemented sliding-window chunking.
- [ ] Compared retrieval performance with different chunk sizes.

### Metadata & Filtering
- [ ] Indexed documents with metadata (e.g., author, year).
- [ ] Implemented queries with filters (metadata + semantic similarity).

### Hybrid Search
- [ ] Implemented BM25 lexical ranking.
- [ ] Implemented semantic search using embeddings.
- [ ] Combined BM25 and embeddings into a hybrid score.
- [ ] Validated results with test queries.

### Consolidation
- [ ] Answered all questions in `04_conceptual_questions.md`.
- [ ] **Self-eval:** I can explain in plain words:
  - Why chunking is important.
  - When to use metadata filtering.
  - The difference between lexical, semantic, and hybrid search.
