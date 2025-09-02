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

## Deliverables
- `env/requirements.txt` frozen.
- Dataset tracked with DVC (`.dvc` file).
- MLflow run with metrics & artifacts logged.
- Reproducibility test passing.
- `04_conceptual_questions.md` answered.

---

## Folder layout (Week 09)
```
02-mlops-infra/
  week-09-versioning-and-tracking/
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
      01_dvc_basics.py
      02_mlflow_tracking.py
      03_reproducibility_test.py
      04_conceptual_questions.md
```
