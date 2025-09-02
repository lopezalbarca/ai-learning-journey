"""
03_metrics.py

Compute lightweight metrics: relevance, faithfulness, coverage.
Currently placeholder logic; extend with embedding similarity or LLM-as-a-judge.
"""

import json
from sklearn.metrics import precision_score

def simple_string_overlap(a: str, b: str) -> float:
    set_a, set_b = set(a.lower().split()), set(b.lower().split())
    return len(set_a & set_b) / max(1, len(set_b))

def evaluate():
    with open("eval_results.json", encoding="utf-8") as f:
        results = json.load(f)

    for r in results:
        gold, pred = r["gold"], r["pred"]
        r["coverage"] = simple_string_overlap(pred, gold)
        # Faithfulness/relevance would normally need embeddings or LLM-as-judge
        r["faithfulness"] = 1.0
        r["relevance"] = 1.0

    with open("eval_metrics.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    evaluate()
    print("✅ Metrics computed and saved to eval_metrics.json")
