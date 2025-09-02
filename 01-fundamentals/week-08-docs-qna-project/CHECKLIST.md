# W08 · Checklist

### Setup
- [ ] Virtual environment created and activated.
- [ ] Dependencies installed (`env/requirements.base.txt`).
- [ ] `env/requirements.txt` generated and committed.

### Ingest & Index
- [ ] `01_ingest.py` parses docs, chunks, attaches metadata.
- [ ] Embeddings generated and stored (FAISS or Qdrant).

### Retrieval
- [ ] `02_retrieval.py` returns top‑k passages + metadata.
- [ ] Retrieved context is logged for inspection.

### Generation (Grounded)
- [ ] `03_generation.py` produces grounded answers with `[S#]` citations.
- [ ] Generator returns a **structured result**: `answer`, `citations`, `latency_ms`, `usage` (tokens).

### Evaluation
- [ ] Evalset (5–10 Q/A) defined.
- [ ] `04_eval.py` computes **faithfulness**, **relevance**, **coverage**.
- [ ] Results saved to CSV/Markdown.

### Report
- [ ] `05_report.md` completed with metrics and reflections.

### Pro Mode — Product‑Minded Add‑Ons
- [ ] **Traceability:** Streamlit UI includes **“Show retrieved context”** that reveals exact chunks + metadata.
- [ ] **Cost/Performance:** Per‑query CSV logs with `latency_ms` and token `usage` (prompt/completion/total).
- [ ] **Cache:** Simple cache by `(query, retriever_params)` with hit/miss stats.

### Consolidation
- [ ] I can explain how ingestion, retrieval, generation, and evaluation connect.
- [ ] I can describe strengths/limits of my Q&A pipeline and how I’d harden it for production.
