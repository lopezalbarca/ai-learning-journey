"""
Exercise 01 · DVC Basics

Task:
- Create a small dataset with pandas (e.g., CSV with random numbers).
- Save it as `data.csv`.
- Use DVC to track the file (`dvc add data.csv`).

Notes:
- Commit the generated `.dvc` file to git.
- Optional: configure a remote (S3, local folder).
"""

import pandas as pd
import numpy as np

# Generate small dataset
df = pd.DataFrame({
    "x": np.arange(10),
    "y": np.random.randint(0, 100, size=10)
})
df.to_csv("data.csv", index=False)
print("Dataset saved to data.csv (now track with DVC).")
