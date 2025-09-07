# W08 · Documents Q&A Project (Fundamentals + .NET Orchestration)

**Goal:** Consolidate everything learned in Weeks 3–7 into a working end-to-end **Documents Q&A pipeline**, and take the first step toward **production-minded orchestration**:
- Ingest documents → chunk → embed → index (FAISS/Qdrant).
- Retrieve top-k passages.
- Generate grounded answers with citations.
- Evaluate with lightweight metrics.
- Write a short project report.
- **NEW:** Orchestrate the Python pipeline with a **.NET Minimal API** (resilience with Polly).
- **NEW:** Run the whole stack via **Docker Compose** (Qdrant + FastAPI + .NET API).
- **Pro Mode:** Add **traceability (Show Context)**, **latency/token logging**, and a **simple cache**.

---

## Learning outcomes
- Build a mini retrieval-augmented QA system over your own documents.
- Apply **retrieval + generation + evaluation** in a single pipeline.
- Compute metrics (**faithfulness**, **relevance**, **coverage**).
- Orchestrate Python services with a **.NET API** and resilience policies.
- Run the system in **containers** with Docker Compose.
- **Pro Mode:** Debug with Show Context, monitor costs/latency, and apply caching.

---

## Architecture (this week)
```
week-08-docs-qna-project/
├─ docker-compose.yml
├─ python-service/             # FastAPI service exposing /ingest and /qa
│  ├─ Dockerfile
│  ├─ requirements.txt
│  └─ app/main.py
├─ src/DocsQna.Api/            # .NET 8 Minimal API (Polly + metrics)
│  ├─ DocsQna.Api.csproj
│  ├─ Program.cs
│  └─ Dockerfile
├─ exercises/                  # lab code: ingest, retrieval, generation, eval, report
├─ app.py                      # Streamlit UI (Show Context + logging + cache)
└─ runs/metrics.csv            # per-query logs (timestamp, latency, tokens, cache_hit)
```

**Flow:**  
Streamlit (front) → **DocsQna.Api (.NET)** → **py-rag (FastAPI/Python)** → Qdrant/OpenAI → back to .NET → Streamlit

---

## Plan: Your Step-by-Step Guide

### 1) Prepare Your Lab (for exercises)
```bash
python -m venv .venv
source .venv/bin/activate      # Mac/Linux
.venv\Scripts\Activate.ps1     # Windows

pip install -r env/requirements.base.txt
pip freeze > env/requirements.txt
```
Base deps: `openai`, `numpy`, `pandas`, `faiss-cpu`, `qdrant-client`, `scikit-learn`, `tqdm`, `streamlit`, `diskcache`.

> The **FastAPI service** has its own `requirements.txt` inside `python-service/` and is built via Docker.

---

### 2) Run the stack (Docker Compose)
```bash
# from week-08-docs-qna-project/
export OPENAI_API_KEY=sk-...    # Windows: setx OPENAI_API_KEY "sk-..."
docker compose build
docker compose up
```

Health checks:
- **.NET API** → `GET http://localhost:8080/`
- **FastAPI (py-rag)** → `GET http://localhost:8000/docs`
- **Qdrant** → `GET http://localhost:6333/`

---

### 3) Ingest & Index (wire your code)
Open `python-service/app/main.py` and connect it to your exercise logic:
- Parse docs, chunk, attach metadata (`doc_id`, `chunk_id`, `source`).
- Embed and upsert into Qdrant.

Example contract:
```http
POST /ingest
{ "paths": ["doc1.md", "doc2.pdf"] }
→ { "ok": true, "ingested": 12 }
```

---

### 4) Retrieval & Generation
Wire `/qa` to your retrieval + generation logic:
- Retrieve top-k passages.
- Generate answer with citations (`[S1]`, `[S2]`).
- Return structured response including metrics.

Example contract:
```http
POST /qa
{ "query": "What is this project about?", "topk": 5 }
→ {
  "answer": "... with [S1][S2]",
  "citations": { "S1": {"doc_id":"...", "chunk_id":3}, ... },
  "latency_ms": 842.3,
  "usage": { "prompt_tokens": 321, "completion_tokens": 102, "total_tokens": 423 },
  "retrieved": [
    { "id":"S1", "score":0.82, "meta":{...}, "text":"..." }
  ]
}
```

---

### 5) .NET API Orchestration
- Proxies `/api/ingest` → Python `/ingest`  
- Proxies `/api/qa` → Python `/qa`  
- Uses **Polly** policies: retry with backoff, timeout, circuit-breaker.  
- Logs metrics (`qa_requests_total`, `qa_latency_ms`).  

---

### 6) Streamlit UI (Pro Mode)
- Calls `.NET /api/qa`, not the LLM directly.  
- Toggle **“Show retrieved context”** reveals chunks + metadata.  
- Logs per query → `runs/metrics.csv`.  
- Adds a simple cache (`diskcache` or in-memory dict).  

---

### 7) Evaluation
- Define evalset (5–10 Q/A).  
- Run `exercises/04_eval.py` to compute **faithfulness, relevance, coverage**.  
- Save results in CSV/Markdown.  
- Summarize in `exercises/05_report.md`.

---

## Deliverables
- `env/requirements.txt` frozen.
- All exercise scripts runnable.
- **Docker Compose stack** running (`qdrant`, `py-rag`, `.NET api`).
- `/ingest` and `/qa` endpoints working.
- Streamlit with Show Context + logging + cache.
- `runs/metrics.csv` populated with real queries.
- Evaluation results + `05_report.md`.

---

## Tips
- Keep API contracts stable (`/qa` response shape).  
- Start with FAISS for simplicity, migrate to Qdrant for production features.  
- Measure before optimizing: `latency_ms`, `total_tokens`, and `cache_hit` tell the story.
