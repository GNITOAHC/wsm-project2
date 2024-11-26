import matplotlib.pyplot as plt

# fmt: off
models = [
    "BM25 Porter", "BM25 Krovetz", "BM25 None",
    "LMMLE Porter", "LMMLE Krovetz", "LMMLE None",
    "LMJM Porter", "LMJM Krovetz", "LMJM None",
    "DFR In L H3 Porter", "DFR In L Z Porter"
]

precision_at_10 = [
    0.3600, 0.1875, 0.1375,
    0.3800, 0.1650, 0.1375,
    0.3150, 0.1575, 0.1225,
    0.4100, 0.3475
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
