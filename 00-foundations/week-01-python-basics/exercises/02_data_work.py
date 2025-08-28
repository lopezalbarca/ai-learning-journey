# %% [markdown]
# # Light data work with pandas (guided)
# Tasks: load the CSV, filter rows, compute aggregates, produce a chart, and save results.

# %%
import pandas as pd
import matplotlib.pyplot as plt

csv_path = "exercises/data/movies_sample.csv"

# TODO 1: load the CSV into a DataFrame named df
# df = ...

# TODO 2: show a quick preview (head) and numeric summary (describe)
# print(...)
# print(...)

# %% [markdown]
# ## Filter: year >= 2000 and rating >= 7.5

# %%
# TODO 3: create a DataFrame `modern_good` with the filter above and display first 10 rows
# modern_good = ...
# print(modern_good[["title", "year", "rating"]].head(10))

# Basic checks (uncomment when implemented)
# assert (modern_good["year"] >= 2000).all()
# assert (modern_good["rating"] >= 7.5).all()

# %% [markdown]
# ## Top 5 by rating

# %%
# TODO 4: compute the Top 5 rows by rating (descending)
# top_5 = ...
# print(top_5)

# TODO 5: save the Top 5 to CSV (top_5_movies.csv)
# top_5.to_csv("exercises/data/top_5_movies.csv", index=False)

# %% [markdown]
# ## Chart: average rating by decade

# %%
# TODO 6: create a decade column (e.g., 1990, 2000, ...),
# group by decade and plot the mean rating as a bar chart.
# Hint: (df["year"] // 10) * 10
# (
#   df.assign(decade=...)
#     .groupby("decade")["rating"].mean()
#     .plot(kind="bar", title="Average rating by decade")
# )
# plt.tight_layout()
# plt.show()
