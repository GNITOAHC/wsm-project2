import matplotlib.pyplot as plt

# fmt: off
models = [
    "BM25 Porter", "BM25 Krovetz", "BM25 None",
    "LMMLE Porter", "LMMLE Krovetz", "LMMLE None",
    "LMJM Porter", "LMJM Krovetz", "LMJM None"
]

precision_at_10 = [
    0.3700, 0.1200, 0.0700,
    0.3400, 0.1100, 0.0600,
    0.3700, 0.0900, 0.0400
]
# fmt: on

# Plot
plt.figure(figsize=(10, 6))
plt.bar(models, precision_at_10, color="skyblue", edgecolor="black")
plt.title("Precision at Rank 10 for Various Models", fontsize=16)
plt.xlabel("Models", fontsize=14)
plt.ylabel("Precision at Rank 10", fontsize=14)
plt.xticks(rotation=45, ha="right")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()

# Display
plt.show()
