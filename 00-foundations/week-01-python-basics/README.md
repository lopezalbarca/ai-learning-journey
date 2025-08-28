# W01 · Python Basics (Foundations)

**Goal:** Build enough Python fluency to prototype quickly (Jupyter) and handle light data work with clean, reproducible environments.

## Learning outcomes
- Create and activate a virtual environment.
- Install base packages and **freeze** exact dependencies to `env/requirements.txt`.
- Refresh core Python syntax (types, collections, control flow, functions, comprehensions, basic error handling).
- Perform light data wrangling with `pandas` and basic plotting with `matplotlib`.
- Reproduce the environment from scratch using `requirements.txt`.

---

## Prerequisites
- Python **3.11+**
- VS Code (or Code Server) with Python extension

---

## Plan: Your Step-by-Step Guide

### 1) Environment setup (manual learning path)
> Recommended the first time to understand what the scripts do.

```bash
# create and activate venv
python -m venv .venv
# Linux/Mac
source .venv/bin/activate
# Windows PowerShell
# .\.venv\Scripts\Activate.ps1

# upgrade pip
python -m pip install --upgrade pip

# install base packages for this week
pip install -r env/requirements.base.txt

# jupyter for notebooks
pip install jupyter
```

**Freeze exact versions** (reproducibility):
```bash
pip freeze > env/requirements.txt
```

> 🔎 Why freeze? You capture exact versions that worked for you. Later, you (or CI) can rebuild the same environment with `pip install -r env/requirements.txt`.

**Docs & references**
- Python tutorial: https://docs.python.org/3/tutorial/
- PEP 8 (style guide): https://peps.python.org/pep-0008/

---

### 2) (Optional) One-shot setup via scripts
Use these after you’ve done the manual steps once and understand them.

```bash
# Linux/Mac
bash env/setup.sh

# Windows PowerShell
./env/setup.ps1
```

Scripts will: create venv, install base packages + jupyter, and **freeze** to `env/requirements.txt`.

---

### 3) Python fundamentals refresh (guided katas)
Open and complete:
```
exercises/01_syntax_katas.py
```
- Fill the **TODOs**.
- Run the file; quick asserts at the bottom should pass.

**Focus areas**
- Types: `int`, `float`, `str`, `bool`
- Collections: `list`, `dict`, `set`, `tuple`
- Control flow: `if/elif/else`, `for`, `while`
- Functions and arguments
- List/dict comprehensions
- Basic exception handling (`try/except`)

---

### 4) Light data work with pandas (guided + TODOs)
Open:
```
exercises/02_data_work.py
```
- Load the provided CSV: `exercises/data/movies_sample.csv`
- Explore (`head`, `describe`)
- Filter rows (e.g., `year >= 2000` and `rating >= 7.5`)
- Compute a **Top 5 by rating**
- **New step:** Save the Top 5 into a new CSV file (`top_5_movies.csv`) in the same folder
- Create a **bar chart**: average rating by decade

**Docs**
- pandas Getting Started: https://pandas.pydata.org/docs/getting_started/
- Matplotlib tutorials: https://matplotlib.org/stable/tutorials/

---

### 5) Reproducibility checkpoint
Rebuild from scratch using your frozen dependencies:
```bash
# deactivate if active, then remove the venv folder
# Linux/Mac
deactivate || true
rm -rf .venv

# Windows PowerShell (from repo root)
# Deactivate in your shell, then:
# Remove-Item -Recurse -Force .venv

# recreate and install from the frozen file
python -m venv .venv
# activate (see step 1)
python -m pip install --upgrade pip
pip install -r env/requirements.txt

# sanity check
python -c "import numpy, pandas, matplotlib; print('OK')"
```

---

## Deliverables
- `env/requirements.txt` generated via `pip freeze`.
- All asserts passing in `exercises/01_syntax_katas.py`.
- A plot produced in `exercises/02_data_work.py` (shown or saved).
- `top_5_movies.csv` created with the filtered data.

---

## How to run
```bash
# Open the folder in VS Code
code .

# or start Jupyter
jupyter notebook
```

---

## Folder layout (Week 01)
```
00-foundations/
  week-01-python-basics/
    README.md
    CHECKLIST.md
    .gitignore
    env/
      setup.ps1
      setup.sh
      requirements.base.txt
      requirements.txt    # generated
    resources/
      links.md
    exercises/
      01_syntax_katas.py
      02_data_work.py
      data/
        movies_sample.csv
    solutions/
      .gitkeep
```
