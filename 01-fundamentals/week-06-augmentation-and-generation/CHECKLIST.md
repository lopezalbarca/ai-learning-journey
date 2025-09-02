# W06 · Checklist

### Setup
- [ ] Virtual environment created and activated.
- [ ] Dependencies installed (`numpy`, `openai`, `faiss-cpu`, `qdrant-client`, `rank-bm25`, `sentence-transformers`).
- [ ] `env/requirements.txt` generated and committed.

### Re-ranking
- [ ] First-pass retrieval working (reuse W05 or toy docs).
- [ ] Cross-encoder reranker applied to re-order top candidates.
- [ ] Latency and quality vs. baseline observed.

### Passage Fusion
- [ ] Deduplication and key-sentence extraction implemented.
- [ ] Fused context built under a clear token budget.
- [ ] Answer quality compared: raw top-k vs. fused context.

### Context Building & Grounding
- [ ] Context ordering strategy implemented (score/section/recency).
- [ ] Sources tagged (e.g., `[S1]`) and citation map kept.
- [ ] Guardrail: refuse / ask for more info if evidence is insufficient.
- [ ] Output format enforces citations and/or quotes.

### Reducing Hallucinations
- [ ] Prompts include explicit instructions to cite sources.
- [ ] JSON schema (or structured) outputs where appropriate.
- [ ] Calibrated refusal implemented when confidence is low.
- [ ] Prefer extractive spans over generative summaries when possible.

### Lightweight Evaluation
- [ ] Tiny eval set (5–10 Q/A) created.
- [ ] Baseline vs. reranked vs. fused compared on simple metrics.
- [ ] Results recorded (CSV/Markdown) and brief takeaways written.

### Consolidation
- [ ] I can explain: cross-encoder vs. bi-encoder, what passage fusion achieves, and why citations reduce hallucinations.
- [ ] I can describe a practical context-building strategy for my domain.
