# exercises/word_vectors.py
import numpy as np

# These are example vectors (simplified for clarity) from a pre-trained GloVe model.
# In a real-world scenario, these vectors would have more dimensions (e.g., 300).
word_embeddings = {
    'rey': np.array([0.92, 0.45, 0.18]),
    'reina': np.array([0.85, 0.65, 0.25]),
    'hombre': np.array([0.88, 0.15, 0.05]),
    'mujer': np.array([0.79, 0.38, 0.15]),
    'palacio': np.array([0.65, 0.51, 0.72]),
    'casa': np.array([0.21, 0.49, 0.68]),
}