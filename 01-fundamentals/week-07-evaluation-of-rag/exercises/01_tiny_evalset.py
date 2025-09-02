"""
01_tiny_evalset.py

Define a small evaluation dataset (5–10 Q/A pairs).
Save as JSON or CSV for later use.
"""

import json

def create_evalset():
    dataset = [
        {"question": "What is RAG?", "answer": "Retrieval-Augmented Generation, a method that combines document retrieval with LLM generation."},
        {"question": "What does faithfulness mean in RAG evaluation?", "answer": "The answer must not hallucinate and should stick to retrieved context."},
    ]
    with open("evalset.json", "w", encoding="utf-8") as f:
        json.dump(dataset, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    create_evalset()
    print("✅ Evalset saved to evalset.json")
