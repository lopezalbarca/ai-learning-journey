"""
Exercise 03 · Reproducibility Test

Task:
- Run the same experiment twice with same random seed → same results.
- Change the seed → results differ.
"""

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def run_experiment(seed=42):
    np.random.seed(seed)
    X = np.random.rand(100, 3)
    y = (X[:, 0] + X[:, 1] > 1).astype(int)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=seed)
    model = LogisticRegression()
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    return acc

print("Run with seed=42:", run_experiment(42))
print("Run again with seed=42:", run_experiment(42))
print("Run with seed=123:", run_experiment(123))
