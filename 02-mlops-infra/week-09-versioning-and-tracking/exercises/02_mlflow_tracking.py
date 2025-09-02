"""
Exercise 02 · MLflow Tracking

Task:
- Train a simple sklearn model (e.g., LogisticRegression).
- Log parameters, metrics, and the model using MLflow.
- Run `mlflow ui` and check results.

"""

import mlflow
import mlflow.sklearn
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Generate fake dataset
X = np.random.rand(100, 3)
y = (X[:, 0] + X[:, 1] > 1).astype(int)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

mlflow.set_experiment("week09_tracking_demo")

with mlflow.start_run():
    C = 1.0
    model = LogisticRegression(C=C)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)

    mlflow.log_param("C", C)
    mlflow.log_metric("accuracy", acc)
    mlflow.sklearn.log_model(model, "model")

    print(f"Logged run with accuracy: {acc:.3f}")
