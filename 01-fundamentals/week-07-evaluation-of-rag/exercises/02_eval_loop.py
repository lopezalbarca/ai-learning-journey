"""
02_eval_loop.py

Run evaluation loop: for each question, call your RAG pipeline and store answers.
Replace the placeholder RAG call with your actual pipeline.
"""

import json

def dummy_rag_answer(question: str) -> str:
    # TODO: Replace with real RAG call (retriever + generator)
    return f"[Dummy answer for] {question}"

def run_eval_loop():
    with open("evalset.json", encoding="utf-8") as f:
        dataset = json.load(f)

    results = []
    for item in dataset:
        q = item["question"]
        gold = item["answer"]
        pred = dummy_rag_answer(q)
        results.append({"question": q, "gold": gold, "pred": pred})

    with open("eval_results.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    run_eval_loop()
    print("✅ Eval loop completed, results saved to eval_results.json")
