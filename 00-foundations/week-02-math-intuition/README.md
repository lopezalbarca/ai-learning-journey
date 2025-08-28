# W02 · Math Intuition (Foundations)

**Goal:** Build the core mental models to understand *how* modern AI works. This week is less about coding and more about grasping the key intuitions behind vectors, semantic similarity, and the Transformer architecture.

## Learning outcomes
- Explain what a vector embedding is using a real-world analogy.
- Calculate vector similarity using Dot Product and Cosine Similarity with `numpy`.
- Understand *why* Cosine Similarity is often preferred for semantic search.
- Explain the concept of Self-Attention with a simple sentence.
- Feel comfortable with the core ideas that you'll be applying in the coming weeks.

---

## Plan: Your Step-by-Step Guide

Follow these steps in order. Each step builds on the previous one, from visual idea to code and theory.

### 1) Prepare Your Lab (Manual Path)
> **Goal:** Understand the setup process by doing it by hand once.

1.  Open your terminal in this folder (`week-02-math-intuition`).
2.  Create and activate a new virtual environment:
    ```bash
    # Create the environment
    python -m venv .venv
    # Activate it (e.g., in PowerShell)
    .\.venv\Scripts\Activate.ps1
    ```
3.  Install base dependencies and freeze them into a `requirements.txt`:
    ```bash
    # Upgrade pip
    python -m pip install --upgrade pip
    # Install from the base file
    pip install -r env/requirements.base.txt
    # Important! Generate the exact versions file
    pip freeze > env/requirements.txt
    ```

### 2) (Optional): One-Shot Setup via Scripts
> **Goal:** Use scripts to automate the setup process for future runs, maintaining symmetry with Week 1.

Once you understand the manual steps, you can use these scripts to do it all in one go.

```bash
# On Linux/Mac
bash env/setup.sh

# On Windows PowerShell
./env/setup.ps1
```

### 3) Visualize the Vectors
> **Goal:** Intuitively understand what vectors are and how they interact, focusing on the geometry.

**Action:** Watch these three essential videos from **3Blue1Brown**. Focus on the animations, not the formulas.

1.  [**Vectors (Chapter 1, Essence of linear algebra)**](https://www.youtube.com/watch?v=fNk_zzaMoSs)
2.  [**Linear combinations, span (Chapter 2)**](https://www.youtube.com/watch?v=k7RM-ot2NWY)
3.  [**Dot products and duality (Chapter 9)**](https://www.youtube.com/watch?v=LyGKycYT2v0)

### 4) From Intuition to Code
> **Goal:** Solidify the concepts you just saw by implementing them in Python.

**Action:** Open the exercise file and complete Part 1.
```
exercises/01_similarity_calculator.py  (Part 1: Similarity Functions)
```
- **Your task:** Fill in the `TODOs` to implement the `dot_product` and `cosine_similarity` functions using `numpy`.

### 5) The "Wow" Moment - The Magic of Embeddings
> **Goal:** See a practical and almost magical application of vector math on language.

**Action:** Continue in the same exercise file.
```
exercises/01_similarity_calculator.py  (Part 2: 'King - Man + Woman' Analogy)
```
- **Context:** We will use a small dictionary of real word vectors provided in `exercises/word_vectors.py`.
- **Your task:**
    1.  Import the `word_embeddings` dictionary.
    2.  Perform the operation: `result_vector = vector('rey') - vector('hombre') + vector('mujer')`.
    3.  Use your `cosine_similarity` function to find which word in our dictionary is closest to your `result_vector`.

### 6) Understanding the Engine of LLMs
> **Goal:** Get a high-level, conceptual understanding of the Transformer architecture and Self-Attention.

**Action:** Watch and read these two legendary resources.

1.  **Watch:** [The Transformer & Attention Mechanism, Clearly Explained!!! (by StatQuest)](https://www.youtube.com/watch?v=eMlx5fFNoYc)
2.  **Read:** [The Illustrated Transformer (blog post by Jay Alammar)](http://jalammar.github.io/illustrated-transformer/)

### 7) Consolidate Your Knowledge
> **Goal:** Force yourself to explain what you've learned, which is the best way to ensure you've truly understood it.

**Action:** Open and answer the questions in this file:
```
exercises/02_conceptual_questions.md
```
**Pro-Tip for Deep Learning:** Don't just write the answers. Try to **explain the concepts in your own words out loud**, as if you were teaching it to a colleague. You can even record a 1-minute audio with your phone for each concept. This is a powerful technique called the Feynman Technique to solidify knowledge.

---
## Deliverables
- `env/requirements.txt` generated and saved.
- `exercises/01_similarity_calculator.py` completed, with all asserts passing.
- `exercises/02_conceptual_questions.md` with well-reasoned answers.
- **Conceptual Understanding:** I can confidently explain, in my own words, what an embedding is, why cosine similarity is useful, and what the core idea of self-attention is.