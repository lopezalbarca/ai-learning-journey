# W04 · Embeddings & Vector Stores (Fundamentals)

**Goal:** Understand what embeddings represent, how similarity search works, and how vector databases store them. Build a small semantic search system from scratch.

---

## Learning outcomes
- Explain in your own words what an embedding is.
- Generate embeddings with an API (e.g., OpenAI).
- Compute cosine similarity between vectors.
- Build a simple in-memory semantic search engine.
- Store embeddings in FAISS (local) and Qdrant (vector DB).
- Understand why we need vector stores instead of just relational DBs.

---

## Prerequisites
- Python **3.11+**
- OpenAI API key exported as environment variable:  
  ```bash
  export OPENAI_API_KEY="your_api_key"
  ```

---

## Plan: Your Step-by-Step Guide

### 0) Important Reminder — Vector Dimensions
**Goal:** Ensure you understand why embeddings must be consistent.  

- All embeddings you compare **must come from the same model**, otherwise their dimensions (and semantic space) won’t match.  
- Example: `text-embedding-3-small` → 1536 dimensions; `all-MiniLM-L6-v2` → 384 dimensions.  
- Mixing them makes cosine similarity meaningless.

---

### 1) Prepare Your Lab
**Goal:** Be ready to generate embeddings and store them.  

1. Create and activate `.venv`.
2. Install dependencies:
   ```bash
   pip install -r env/requirements.base.txt
   pip freeze > env/requirements.txt
   ```
   Base deps: `numpy`, `openai`, `faiss-cpu`, `qdrant-client`.

---

### 2) Build Mental Models
**Goal:** Grasp what embeddings represent (geometry + intuition).  

- 📺 Watch: [3Blue1Brown — Vectors in higher dimensions](https://www.youtube.com/watch?v=TgKwz5Ikpc8)  
- 📖 Read: [Jay Alammar — The Illustrated Word2Vec](https://jalammar.github.io/illustrated-word2vec/)  

---

### 3) Hands-On with Embeddings
**Goal:** Generate and compare embeddings.  

Open:
```
exercises/01_basic_embeddings.py
```
Tasks:
- Call OpenAI’s `text-embedding-3-small`.
- Compute cosine similarity manually.
- Compare “king”, “queen”, “man”, “woman”.

---

### 4) Semantic Search in Memory
**Goal:** Build your first retrieval system.  

Open:
```
exercises/02_semantic_search.py
```
Tasks:
- Create a small doc set (5–10 short texts).
- Embed and store in memory (list of vectors).
- Given a query, compute cosine similarity and return top-k docs.

---

### 5) Store in FAISS
**Goal:** Use a real vector store for speed and scaling.  

Open:
```
exercises/03_vector_store.py
```
Tasks:
- Install FAISS (`faiss-cpu`).
- Create an index, insert embeddings.
- Query top-k similar vectors.

---

### 6) Store in Qdrant
**Goal:** Learn how a production-grade vector DB works.  

Open:
```
exercises/03_vector_store.py  (second part)
```
Tasks:
- Run Qdrant locally with Docker (`qdrant/qdrant`).
- Or sign up for [Qdrant Cloud free tier](https://qdrant.tech/).
- Use `qdrant-client` to insert/query vectors.

---

### 7) Wrap-Up & Reflection
**Goal:** Ensure conceptual clarity.  

Open:
```
exercises/04_conceptual_questions.md
```
Questions:
- What do embeddings represent?
- Why is cosine similarity preferred in semantic search?
- What’s the difference between FAISS and Qdrant?
- Why can’t we just use PostgreSQL/MySQL for this?

---

## Deliverables
- `env/requirements.txt` generated.
- Completed scripts:
  - `01_basic_embeddings.py`
  - `02_semantic_search.py`
  - `03_vector_store.py`
- `04_conceptual_questions.md` answered.
- I can explain embeddings and vector stores clearly in my own words.

---

## Folder layout (Week 04)
```
01-fundamentals/
  week-04-embeddings-and-vector-stores/
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
      01_basic_embeddings.py
      02_semantic_search.py
      03_vector_store.py
      04_conceptual_questions.md
```
