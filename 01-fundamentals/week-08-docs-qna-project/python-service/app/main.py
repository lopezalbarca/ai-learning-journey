from fastapi import FastAPI
from pydantic import BaseModel
import time

app = FastAPI(title="Week08 Py RAG")

class IngestRequest(BaseModel):
    paths: list[str]

class QaRequest(BaseModel):
    query: str
    topk: int = 5

@app.post("/ingest")
def ingest(req: IngestRequest):
    return {"ok": True, "ingested": len(req.paths)}

@app.post("/qa")
def qa(req: QaRequest):
    start = time.time()
    answer = f"Demo answer for: {req.query}"
    latency_ms = (time.time() - start) * 1000
    return {
        "answer": answer,
        "citations": {"S1": {"doc_id": "demo", "chunk_id": 0}},
        "latency_ms": latency_ms,
        "usage": {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0}
    }
