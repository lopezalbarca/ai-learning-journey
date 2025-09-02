# W07 · Evaluation of RAG (Fundamentals)

**Goal:** Learn to evaluate Retrieval-Augmented Generation (RAG) systems beyond “looks good.” Build an evaluation mindset and lightweight loop covering *faithfulness*, *relevance*, and *coverage*.

---

## Learning outcomes
- Differentiate **faithfulness**, **relevance**, and **coverage** in RAG answers.
- Create a tiny evaluation dataset (5–10 Q/A pairs).
- Implement a simple evaluation loop: retrieval → generation → evaluation.
- Compute lightweight metrics (precision@k, coverage %, groundedness).
- Record results in CSV/Markdown for comparison.
- Understand trade-offs between human vs. automated evaluation (LLM-as-a-judge).

---

## Prerequisites
- Python **3.11+**
- OpenAI API key exported as environment variable:  
  ```bash
  export OPENAI_API_KEY="your_api_key"
  ```

---

## Plan: Your Step-by-Step Guide

### 1) Prepare Your Lab
**Goal:** Set up dependencies for evaluation.
```bash
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
# .venv\Scripts\Activate.ps1   # Windows PowerShell

pip install -r env/requirements.base.txt
pip freeze > env/requirements.txt
```

Dependencies: `openai`, `numpy`, `pandas`, `scikit-learn`, `tqdm`.

---

### 2) Create a Tiny Eval Set
**Goal:** Define a small but meaningful dataset for evaluation.

Open:
```
exercises/01_tiny_evalset.py
```
Tasks:
- Define 5–10 Q/A pairs relevant to your domain (or toy examples).
- Save them as JSON or CSV.

---

### 3) Build an Evaluation Loop
**Goal:** Run questions through your RAG system and collect answers.

Open:
```
exercises/02_eval_loop.py
```
Tasks:
- For each question, run retrieval → generation.
- Save model answers alongside gold answers.

---

### 4) Implement Metrics
**Goal:** Automate simple evaluation.

Open:
```
exercises/03_metrics.py
```
Tasks:
- Compute **faithfulness** (does answer hallucinate? → rule-based or GPT-as-judge).
- Compute **relevance** (semantic similarity to gold).
- Compute **coverage** (how much of gold facts appear).
- Save results as CSV/Markdown.

---

### 5) Reflection & Conceptual Questions
Open:
```
exercises/04_conceptual_questions.md
```
Questions:
- Why is “looks correct to me” insufficient for evaluation?
- What risks arise when using LLM-as-a-judge?
- What are trade-offs between human and automatic evaluation?

---

## Deliverables
- `env/requirements.txt` generated.
- `01_tiny_evalset.py`, `02_eval_loop.py`, `03_metrics.py` implemented.
- Evaluation results recorded (CSV/Markdown).
- `04_conceptual_questions.md` answered with clear reasoning.
- I can explain **faithfulness**, **relevance**, and **coverage** in plain words.

---

## Folder layout (Week 07)
```
01-fundamentals/
  week-07-evaluation-of-rag/
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
      01_tiny_evalset.py
      02_eval_loop.py
      03_metrics.py
      04_conceptual_questions.md
```