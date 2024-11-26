import matplotlib.pyplot as plt

# fmt: off
models = [
    "BM25 Porter", "LMMLE Porter", "DFR GLH2", "DFR INELH2",
    "DFR INLH1", "DFR INLH2", "DFR INLH3", "DFR INLZ"
]

precision_at_10 = [
    0.3700, 0.3400, 0.3450, 0.3325,
    0.3200, 0.3700, 0.4650, 0.3475
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
