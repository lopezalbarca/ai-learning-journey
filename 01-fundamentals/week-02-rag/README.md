# Fundamentals - 02 - RAG (Retrieval-Augmented Generation)

## 🧠 Goal

This week focuses on learning and implementing **Retrieval-Augmented Generation (RAG)**, a powerful technique that combines LLMs with external knowledge bases using vector search.

By the end of the week, I aim to:
- Understand the RAG architecture and its use cases
- Learn how to embed documents and store them in a vector database
- Perform semantic search to retrieve relevant context
- Combine document retrieval with LLM prompts to build a smart Q&A system

---

## 📚 Resources Used (to be completed)

| Resource | Type |
|----------|------|
| [LangChain RAG Docs](https://docs.langchain.com/docs/use-cases/question-answering/) | Docs |
| [Qdrant / Chroma / Pinecone Tutorials] | Vector DB |
| [OpenAI Embeddings Guide](https://platform.openai.com/docs/guides/embeddings) | Docs |
| [YouTube: RAG from scratch with OpenAI](TBD) | Video |
| [C#/.NET Examples (if available)] | SDK / Tutorials |

---

## 📦 Folder Contents

| File / Folder | Description |
|---------------|-------------|
| `README.md` | This file – weekly summary |
| `rag-demo.csproj` | .NET project for testing embeddings + LLM |
| `documents/` | Sample docs used for embedding (PDFs, markdown, etc.) |
| `scripts/` | Scripts for indexing, querying, and retrieval |
| `notes.md` | Personal notes and learnings |

---

## ✅ Progress Log

- [ ] Embedded sample documents using OpenAI embeddings
- [ ] Stored vectors in a local or remote DB (Qdrant / Chroma / Pinecone)
- [ ] Built a retrieval flow: query → search → augment → response
- [ ] Combined it with GPT to answer based on private data

---

## 💡 Notes / Learnings

> - RAG improves response reliability and grounding by injecting context  
> - Quality of embeddings and chunking strategy matters a lot  
> - Simple cosine similarity is powerful when combined with prompt refinement

---

**Next steps:** Move toward a full mini-project where a user can upload documents and get intelligent answers (Week 4).

---

🧠 _“The best prompt is often not written, it’s retrieved.”_