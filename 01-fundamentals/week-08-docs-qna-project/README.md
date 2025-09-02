# W08 · Documents Q&A Project (Fundamentals)

**Goal:** Assemble everything learned in Weeks 3–7 into a working end‑to‑end pipeline:
- Ingest documents.
- Retrieve relevant passages.
- Generate *grounded* answers with citations.
- Evaluate with lightweight metrics.
- Write a short project report.
- (**Pro Mode**) Add **traceability**, **cost/latency metrics**, and a **simple cache** to think like a product.

---

## Learning outcomes
- Build a mini retrieval‑augmented QA system over your own docs.
- Apply **retrieval + generation + evaluation** as a single pipeline.
- Compute basic metrics (**faithfulness**, **relevance**, **coverage**).
- (**Pro Mode**) Add **debuggability (Show Context)**, **token/latency logging**, and **response caching**.

---

## Plan: Your Step‑by‑Step Guide

### 1) Prepare Your Lab
```bash
python -m venv .venv
source .venv/bin/activate      # Mac/Linux
.\.venv\Scripts\Activate.ps1   # Windows
pip install -r env/requirements.base.txt
pip freeze > env/requirements.txt
```

### 2) Ingest & Index Documents
- Open `exercises/01_ingest.py`.
- Parse a small set of documents (txt/pdf/markdown).
- Chunk + attach metadata (`doc_id`, `chunk_id`, `source_path`, etc.).
- Store embeddings in **FAISS** or **Qdrant**.

### 3) Retrieval
- Open `exercises/02_retrieval.py`.
- Given a query, return **top‑k** passages + their metadata.
- Log retrieved context for inspection.

### 4) Generation (with citations)
- Open `exercises/03_generation.py`.
- Prompt the LLM with retrieved context and **tag sources** as `[S1]`, `[S2]`…
- **Return a structured object** with:
  - `answer`: final text
  - `citations`: mapping like `{ "S1": {"doc_id": "...", "chunk_id": ...}, ... }`
  - `latency_ms`: end‑to‑end time for the LLM call
  - `usage`: `{ "prompt_tokens": ..., "completion_tokens": ..., "total_tokens": ... }` (if provided by the API)

**Pseudo‑snippet**
```python
import time

def generate_with_metrics(prompt, client):
    start = time.time()
    resp = client.chat.completions.create(...)
    latency_ms = (time.time() - start) * 1000

    usage = getattr(resp, "usage", None)
    tokens = {}
    if usage:
        tokens = {
            "prompt_tokens": getattr(usage, "prompt_tokens", None),
            "completion_tokens": getattr(usage, "completion_tokens", None),
            "total_tokens": getattr(usage, "total_tokens", None),
        }

    return {
        "answer": resp.choices[0].message.content.strip(),
        "citations": build_citations_map(...),
        "latency_ms": latency_ms,
        "usage": tokens,
    }
```

### 5) Evaluation
- Open `exercises/04_eval.py`.
- Use your evalset (5–10 Q/A).
- Compute **faithfulness, relevance, coverage** (see Week 07).
- Save results to CSV/Markdown.

### 6) Short Report
- Fill `exercises/05_report.md` with:
  - Setup summary
  - Key results (metrics table)
  - Reflection: what worked / what didn’t
  - (**Pro Mode**) Takeaways from latency/token logs & cache hit‑rate

---

## (**Pro Mode**) Product‑Minded Add‑Ons

### A) Traceability / Debuggability (Show Context)
- Build a tiny **Streamlit** UI (`app.py`).
- Add an **expander** or a **toggle**: “**Show retrieved context**”.
- When enabled, display the exact chunks and their metadata that were sent to the LLM.

**Streamlit sketch**
```python
import streamlit as st

st.title("Docs Q&A — Week 08")
q = st.text_input("Ask a question")  # free text input
show_ctx = st.checkbox("🔍 Show retrieved context", value=False)

if q:
    passages = retrieve(q)         # [(text, meta, score), ...]
    result = generate(q, passages) # { answer, citations, latency_ms, usage }

    st.markdown(result["answer"])
    st.caption(f"latency: {result['latency_ms']:.0f} ms · tokens: {result['usage']}")

    if show_ctx:
        with st.expander("Retrieved passages"):
            for i, (text, meta, score) in enumerate(passages, start=1):
                st.markdown(f"**[S{i}]** score={score:.3f} · {meta}")
                st.code(text)
```

### B) Measure Cost & Performance
- Log per‑query metrics to CSV: `timestamp,query,latency_ms,prompt_tokens,completion_tokens,total_tokens,model,topk,reranker,fusion`.
- Use this for later optimization (Phase 2).

### C) Simple Cache
- Add a naive cache keyed by **(query, retriever_params)**. A small **`diskcache`** or in‑memory dict is enough.
- On cache hit, return the stored `{answer, citations, latency_ms, usage}` immediately and **record hit/miss** stats.

---

## Deliverables
- `env/requirements.txt` frozen.
- All scripts in `exercises/` runnable.
- Results recorded in CSV/Markdown.
- `05_report.md` with conclusions.
- (**Pro Mode**) Streamlit app with **Show Context**, CSV logs for **latency/tokens**, and a basic **cache**.

---

## Folder layout (Week 08)
```
01-fundamentals/
  week-08-docs-qna-project/
    README.md
    CHECKLIST.md
    .gitignore
    env/
      setup.ps1
      setup.sh
      requirements.base.txt
      requirements.txt
    resources/
      links.md
    exercises/
      01_ingest.py
      02_retrieval.py
      03_generation.py
      04_eval.py
      05_report.md
    app.py                  # (Pro Mode) Streamlit UI
    runs/                   # CSV logs (latency/tokens/cache)
```
