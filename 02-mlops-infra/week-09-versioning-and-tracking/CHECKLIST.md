# W09 · Checklist

### Setup
- [ ] Virtual environment created and activated.
- [ ] Dependencies installed (`numpy`, `pandas`, `scikit-learn`, `dvc`, `mlflow`).
- [ ] `env/requirements.txt` generated and committed.

### Data Versioning (DVC)
- [ ] DVC initialized (`dvc init`).
- [ ] Dataset tracked (`dvc add data.csv`).
- [ ] Dataset pushed to remote (optional).

### Experiment Tracking (MLflow)
- [ ] `02_mlflow_tracking.py` runs and logs metrics/params/artifacts.
- [ ] MLflow UI shows experiment runs.

### Reproducibility
- [ ] `03_reproducibility_test.py` shows consistent results with same seed.
- [ ] Different seed leads to different results.

### Consolidation
- [ ] `04_conceptual_questions.md` answered.
- [ ] **Self-eval:** I can explain why reproducibility matters in ML projects.
