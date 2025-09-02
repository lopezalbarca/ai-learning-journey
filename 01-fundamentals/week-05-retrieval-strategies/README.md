# W05 · Retrieval Strategies (Fundamentals)

**Goal:** Learn practical strategies for retrieving information from a knowledge base. Go beyond plain vector search by applying chunking, metadata filtering, and hybrid search.

---

## Learning outcomes
- Understand why **chunking** is critical for recall and precision.
- Implement different chunking strategies (fixed size, sliding window).
- Store and query documents with **metadata** (e.g., title, author, year).
- Use **filters** to narrow down results.
- Implement a simple **hybrid search** combining lexical (BM25) and semantic search.

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
**Goal:** Install dependencies and ensure the lab runs smoothly.  
```bash
# Create & activate virtual environment
python -m venv .venv
source .venv/bin/activate  # Mac/Linux
.\.venv\Scripts\Activate.ps1  # Windows PowerShell

# Install dependencies
pip install -r env/requirements.base.txt
pip freeze > env/requirements.txt
```

Dependencies: `numpy`, `openai`, `faiss-cpu`, `qdrant-client`, `rank-bm25`.

---

### 2) Chunking Strategies
**Goal:** See how splitting text affects retrieval.  

Open:
```
exercises/01_chunking.py
```
Tasks:
- Implement fixed-size chunking (by words).
- Implement sliding-window chunking (overlapping).
- Compare retrieval results with different chunk sizes.

---

### 3) Metadata & Filtering
**Goal:** Add structured filtering to improve relevance.  

Open:
```
exercises/02_metadata_filtering.py
```
Tasks:
- Index documents with metadata (author, year).
- Implement queries that filter by metadata + semantic similarity.
- Example: “Find papers about embeddings by *Smith (2021)*.”

---

### 4) Hybrid Search (Lexical + Vector)
**Goal:** Combine BM25 (lexical) and embeddings (semantic).  

Open:
```
exercises/03_hybrid_search.py
```
Tasks:
- Implement BM25 keyword ranking (using `rank-bm25`).
- Compute semantic similarity with embeddings.
- Combine both scores (e.g., weighted average).
- Test on a small set of documents.

---

### 5) Wrap-Up & Reflection
**Goal:** Consolidate your understanding.  

Open:
```
exercises/04_conceptual_questions.md
```
Questions:
- Why does chunking improve retrieval accuracy?
- What are trade-offs between larger vs. smaller chunks?
- When should you use metadata filtering?
- When does hybrid search outperform pure vector search?

---

## Deliverables
- `env/requirements.txt` generated.
- Completed scripts:
  - `01_chunking.py`
  - `02_metadata_filtering.py`
  - `03_hybrid_search.py`
- `04_conceptual_questions.md` answered.
- Clear explanation (in your own words) of when hybrid search is most useful.

---

## Folder layout (Week 05)
```
01-fundamentals/
  week-05-retrieval-strategies/
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
      01_chunking.py
      02_metadata_filtering.py
      03_hybrid_search.py
      04_conceptual_questions.md
```
