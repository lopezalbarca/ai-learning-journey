# W06 · Augmentation & Generation (Fundamentals)

**Goal:** Improve answer quality after retrieval by applying **re‑ranking**, **passage fusion**, and **context building** — and adopt concrete tactics to **reduce hallucinations** in LLM outputs.

---

## Learning outcomes
- Re-rank initial candidates (from BM25/vector/hybrid) with a **cross-encoder** reranker.
- Apply **passage fusion** to merge complementary snippets before prompting.
- Design **context-building** strategies (ordering, dedup, windowing, citations).
- Implement **hallucination-reduction** techniques: cite sources, calibrated refusal, constrained formats.
- Measure impact with a tiny, task-focused evaluation (precision@k / answerable? flags).

---

## Prerequisites
- Python **3.11+**
- An LLM provider key exported as environment variable (e.g., `OPENAI_API_KEY`).

---

## Plan: Your Step-by-Step Guide

### 1) Prepare Your Lab
**Goal:** Set up the env for reranking, fusion, and context experiments.
```bash
# Create & activate virtual environment
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
# .\.venv\Scripts\Activate.ps1  # Windows PowerShell

# Install base deps
pip install -r env/requirements.base.txt
pip freeze > env/requirements.txt
```

Base deps: `numpy`, `openai`, `faiss-cpu`, `qdrant-client`, `rank-bm25`, `sentence-transformers`.

---

### 2) Re-ranking: From Recall to Precision
**Goal:** Upgrade a first-pass retrieval (BM25 / embeddings / hybrid) with a **cross-encoder** that scores *query+passage* pairs.

Open:
```
exercises/01_reranking.py
```
Tasks:
- Take top-20 candidates from any retriever (use your Week 05 code or a toy list).
- Use a cross-encoder (e.g., `cross-encoder/ms-marco-MiniLM-L-6-v2`) to compute relevance scores.
- Return a **re-ranked top-k** list and compare against the original ordering.

**Notes**
- Cross-encoders are slower but usually more precise.
- Keep batch sizes small; log latency and compare with the baseline.

---

### 3) Passage Fusion: Combine Signals Before Prompting
**Goal:** Merge small, complementary passages into a compact, coherent context block that avoids duplication.

Open:
```
exercises/02_passage_fusion.py
```
Tasks:
- Implement simple fusion: deduplicate, sort by score, **extract key sentences**.
- Build a fused context (e.g., ≤ 1,200–1,800 tokens target).
- Compare answering quality using (A) raw top-k vs. (B) fused context.

---

### 4) Context Building & Grounding
**Goal:** Systematically construct the context you pass to the LLM.

Open:
```
exercises/03_context_building.py
```
Tasks:
- Implement ordering strategies (by score, by section, recency).
- Add **source tagging** `[S1], [S2]` and keep a **citations map**.
- Add a **“not enough info” guardrail** (if recall < threshold → ask for more info / refuse).
- Prompt template outputs: **final answer + cited sources**.

---

### 5) Reducing Hallucinations (Practical Tactics)
**Goal:** Adopt concrete, code-enforced practices.
- Ask for **verbatim quotes** and **source IDs** when feasible.
- Use **tight instructions** and **JSON schemas** for outputs.
- Add **calibrated refusal**: if confidence low or no supporting span, say “I don’t know.”
- Prefer **extractive** answers first; only then compose/abstract.

---

### 6) Lightweight Evaluation
**Goal:** Track if changes actually help.
- Create a tiny eval set (5–10 Q/A with gold or “not answerable”).
- For each strategy (baseline vs. rerank vs. fusion): measure **contains-citation?**, **has-support?**, and a simple **precision@k** proxy.
- Record results in a small CSV/Markdown.

---

## Deliverables
- `env/requirements.txt` generated.
- Completed scripts:
  - `01_reranking.py`
  - `02_passage_fusion.py`
  - `03_context_building.py`
- A short table (Markdown/CSV) comparing baseline vs. reranked vs. fused.
- Demonstrated citations in the final answer format (e.g., `[S1],[S3]`).

---

## Folder layout (Week 06)
```
01-fundamentals/
  week-06-augmentation-and-generation/
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
      01_reranking.py
      02_passage_fusion.py
      03_context_building.py
      04_conceptual_questions.md
```
