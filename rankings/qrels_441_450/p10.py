import matplotlib.pyplot as plt

# fmt: off
models = [
    "PorterModel", "CombinationModel", "Top2Model", "PorterMinMaxModel",
    "PorterRobustModel", "PorterWithDfrH3Model_R", "PorterWithDfrH3Model_M", "PorterWithDfrH3Model"
]

precision_at_10 = [
    0.1300, 0.1500, 0.1500, 0.1700,
    0.3000, 0.2900, 0.1900, 0.1400
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
