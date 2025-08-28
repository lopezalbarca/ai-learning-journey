# exercises/01_similarity_calculator.py
import numpy as np
from word_vectors import word_embeddings

# =================================================================
# Part 1: Similarity Functions
# =================================================================

def dot_product(v1, v2):
    """
    Calculates the dot product of two vectors.
    """
    # TODO: Implement the dot product using numpy.
    # Hint: Look for np.dot()
    pass

def cosine_similarity(v1, v2):
    """
    Calculates the cosine similarity between two vectors.
    """
    # TODO: Implement the cosine similarity using numpy.
    # Formula: (v1 . v2) / (||v1|| * ||v2||)
    # Hint: np.linalg.norm() calculates the magnitude (norm) of a vector.
    pass

# --- Assertions for Part 1 ---
v_a = np.array([1, 2, 3])
v_b = np.array([4, 5, 6])
v_c = np.array([-1, 0, 1])

# This block will only run when the script is executed directly
if __name__ == "__main__":
    # Workaround for the functions not being implemented yet
    try:
        assert dot_product(v_a, v_b) == 32, "Dot product calculation is incorrect!"
        assert np.isclose(cosine_similarity(v_a, v_b), 0.9746318), "Cosine similarity calculation is incorrect!"
        assert np.isclose(cosine_similarity(v_a, v_a), 1.0), "Cosine similarity with self should be 1!"
        assert dot_product(v_a, v_c) == 2, "Dot product with negative numbers is incorrect!"
        print("✅ Part 1: All assertions passed!")
    except (AssertionError, TypeError) as e:
        print(f"Part 1 assertions failed: {e}")
        print("--> This is expected until you implement the functions.")


# =================================================================
# Part 2: The "King - Man + Woman" Analogy
# =================================================================

def find_closest_word(start_vec, target_word):
    """
    Finds the word in word_embeddings that is most similar to start_vec.
    """
    best_word = None
    max_similarity = -1

    for word, vec in word_embeddings.items():
        if word == target_word:
            continue # Don't compare the word with itself

        sim = cosine_similarity(start_vec, vec)
        if sim is not None and sim > max_similarity:
            max_similarity = sim
            best_word = word
    
    return best_word

# This block will only run when the script is executed directly
if __name__ == "__main__":
    # TODO:
    # 1. Get the vectors for 'rey', 'hombre', and 'mujer' from the word_embeddings dictionary.
    # 2. Calculate the result_vector = vector('rey') - vector('hombre') + vector('mujer').
    
    rey_vec = None      # Replace None with the actual vector
    hombre_vec = None   # Replace None with the actual vector
    mujer_vec = None    # Replace None with the actual vector
    result_vector = None # Replace None with your calculation

    # --- Find the closest word to your result_vector ---
    # We exclude 'rey' from the search to avoid finding the same starting word.
    if result_vector is not None:
        closest_word = find_closest_word(result_vector, 'rey')

        print(f"\nThe result of 'rey' - 'hombre' + 'mujer' is a vector.")
        print(f"The word in our dictionary most similar to this result is: '{closest_word}'")

        # --- Assertion for Part 2 ---
        assert closest_word == 'reina', "The analogy did not result in 'reina'!"
        print("✅ Part 2: The vector analogy works as expected!")
    else:
        print("\nPart 2 is pending implementation.")