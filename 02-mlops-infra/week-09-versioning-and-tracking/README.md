# W09 · Versioning & Experiment Tracking (MLOps & Infra)

**Goal:** Learn how to version datasets, track experiments, and ensure reproducibility of results.

---

## Learning outcomes
- Use **DVC** to version datasets and artifacts.
- Use **MLflow** to track metrics, parameters, and artifacts.
- Understand the importance of **reproducibility** in ML/AI projects.
- Run the same code with the same data → get the same results.

---

## Prerequisites
- Python **3.11+**
- Git initialized in your repo
- DVC installed and configured (`dvc init`)
- MLflow installed

---

## Plan: Your Step-by-Step Guide

### 1) Prepare Your Lab
```bash
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\Activate.ps1   # Windows PowerShell

pip install -r env/requirements.base.txt
pip freeze > env/requirements.txt
```

Dependencies: `numpy`, `pandas`, `scikit-learn`, `dvc`, `mlflow`

---

### 2) Versioning with DVC
- Initialize DVC in your repo: `dvc init`
- Track a dataset (e.g., `data.csv`):  
  ```bash
  dvc add data.csv
  git add data.csv.dvc .gitignore
  git commit -m "Track dataset with DVC"
  ```
- Push dataset to remote (optional, e.g., S3 or local storage).

---

### 3) Experiment Tracking with MLflow
Open:
```
exercises/02_mlflow_tracking.py
```
Tasks:
- Train a simple sklearn model.
- Log metrics (accuracy, loss).
- Log parameters (learning rate, seed).
- Log the trained model as an artifact.

Run MLflow UI:
```bash
mlflow ui
```
→ navigate to `http://127.0.0.1:5000`

---

### 4) Reproducibility Test
Open:
```
exercises/03_reproducibility_test.py
```
- Run experiment twice with same seed & data → metrics match.
- Change seed → metrics differ.

---

### 5) Conceptual Questions
Open:
```
exercises/04_conceptual_questions.md
```
Reflect on:
- Why is versioning data important?
- What happens if you don’t track hyperparameters?
- How does experiment tracking help team collaboration?

---

### 6) .NET Hook: Serving MLflow

This week also includes a **.NET 9 Minimal API** that proxies MLflow so you can expose experiment data in an enterprise-ready stack.

Steps:
1. Go to: `samples/dotnet/Tracking.Api/`
2. Configure MLflow base URL in `appsettings.json` or via env var:
   ```bash
   export MLflow__BaseUrl=http://localhost:5000
   ```
3. Run the API:
   ```bash
   dotnet run
   # or with Docker
   docker build -t tracking-api:latest .
   docker run -p 8080:8080 -e MLflow__BaseUrl=http://host.docker.internal:5000 tracking-api:latest
   ```
4. Check health: `GET http://localhost:8080/healthz`
5. List experiments: `GET http://localhost:8080/mlflow/experiments`

Endpoints exposed:
- `/mlflow/experiments` → MLflow `experiments/list`
- `/mlflow/runs/{experimentId}` → MLflow `runs/search`
- `/mlflow/runs/{runId}/artifacts` → MLflow `artifacts/list`

Resilience: uses `HttpClientFactory` + Polly retries with backoff and 10s timeout.

Deliverable: prove you can fetch MLflow experiments through the .NET API.

---

## Deliverables
- `env/requirements.txt` frozen.
- Dataset tracked with DVC (`.dvc` file).
- MLflow run with metrics & artifacts logged.
- Reproducibility test passing.
- `04_conceptual_questions.md` answered.
- .NET API (`Tracking.Api`) working and fetching MLflow experiments.
