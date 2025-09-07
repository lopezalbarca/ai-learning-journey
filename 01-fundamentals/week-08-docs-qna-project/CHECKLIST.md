# W08 · Checklist (with .NET Orchestration)

### Setup (Exercises/Streamlit env)
- [ ] Virtual environment created and activated.
- [ ] Dependencies installed (`env/requirements.base.txt`).
- [ ] `env/requirements.txt` generated and committed.

### Containers & Services
- [ ] `docker compose` builds and runs (`qdrant`, `py-rag`, `.NET api`).
- [ ] Healthchecks OK:  
  - http://localhost:8080/ (.NET)  
  - http://localhost:8000/docs (FastAPI)  
  - http://localhost:6333/ (Qdrant)

### Python Service (FastAPI)
- [ ] `/ingest` wired to real ingestion (chunk + embed + upsert).
- [ ] `/qa` wired to retrieval + generation.
- [ ] Response includes: `answer`, `citations`, `latency_ms`, `usage`, and retrieved context.

### .NET API (Orchestration)
- [ ] `/api/ingest` proxies to Python `/ingest`.
- [ ] `/api/qa` proxies to Python `/qa`.
- [ ] **Polly policies** enabled (retry/backoff, timeout, circuit-breaker).
- [ ] Metrics recorded: `qa_requests_total`, `qa_latency_ms`.

### Streamlit UI (Pro Mode)
- [ ] Calls `.NET /api/qa` endpoint.
- [ ] Toggle **“Show retrieved context”** displays chunks + metadata.
- [ ] Cache implemented (in-memory or diskcache).
- [ ] Each query logged in `runs/metrics.csv` (timestamp, query, latency_ms, tokens, cache_hit).

### Evaluation & Report
- [ ] Evalset (5–10 Q/A) defined.
- [ ] `04_eval.py` computes faithfulness, relevance, coverage.
- [ ] Results saved in CSV/Markdown.
- [ ] `05_report.md` completed with metrics and reflections.

### Consolidation
- [ ] I can explain the flow: Streamlit → .NET API → Python service → Qdrant/OpenAI → back.
- [ ] I can reason about latency/cost using the logs in `runs/metrics.csv`.
