"""
Syntax katas — fill the TODOs and run this file.
If everything is fine, you'll see "✅ All katas OK" at the end.

Run:  python exercises/01_syntax_katas.py
"""

# 1) Types & basic operations
def add(a: int, b: int) -> int:
    """Return the sum of a and b."""
    # TODO: implement
    raise NotImplementedError

# 2) Strings
def normalize_name(name: str) -> str:
    """Return capitalized name without leading/trailing spaces."""
    # TODO: implement
    raise NotImplementedError

# 3) List comprehensions
def squares(nums: list[int]) -> list[int]:
    """Return squares using a list comprehension."""
    # TODO: implement
    raise NotImplementedError

# 4) Dicts
def count_words(text: str) -> dict[str, int]:
    """Count whitespace-separated words (case-insensitive)."""
    # TODO: implement
    raise NotImplementedError

# 5) Error handling
def safe_int(value: str, default: int = 0) -> int:
    """Parse an int or return default on ValueError."""
    # TODO: implement
    raise NotImplementedError


# --- Quick tests ---
try:
    assert add(2, 3) == 5
    assert normalize_name("  juan perez  ") == "Juan Perez"
    assert squares([1, 2, 3]) == [1, 4, 9]
    assert count_words("Hola hola Adios") == {"hola": 2, "adios": 1}
    assert safe_int("10") == 10 and safe_int("x", 7) == 7
except NotImplementedError:
    print("❌ Implement the TODOs before running tests.")
    raise

print("✅ All katas OK")
