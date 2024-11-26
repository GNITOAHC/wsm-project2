import matplotlib.pyplot as plt

# Data for un-interpolated average precision across recall levels
# fmt: off
recall = [0.00, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 1.00]
bm25_porter_precision = [0.6626, 0.5298, 0.4591, 0.3644, 0.3149, 0.2582, 0.1820, 0.1220, 0.0584, 0.0222, 0.0137]
bm25_krovetz_precision = [0.3601, 0.3039, 0.2417, 0.1718, 0.1571, 0.1233, 0.0703, 0.0297, 0.0160, 0.0089, 0.0017]
bm25_none_precision = [0.2993, 0.2361, 0.1796, 0.1278, 0.1155, 0.0699, 0.0325, 0.0131, 0.0042, 0.0029, 0.0005]
lmmle_porter_precision = [0.7444, 0.5406, 0.4651, 0.3713, 0.3293, 0.2672, 0.2009, 0.1627, 0.1021, 0.0658, 0.0319]
lmmle_krovetz_precision = [0.3221, 0.2981, 0.2318, 0.1759, 0.1443, 0.1272, 0.0882, 0.0667, 0.0480, 0.0332, 0.0028]
lmmle_none_precision = [0.2715, 0.2397, 0.1893, 0.1251, 0.1015, 0.0896, 0.0421, 0.0299, 0.0234, 0.0204, 0.0013]
lmjm_porter_precision = [0.6471, 0.4330, 0.3482, 0.2721, 0.2255, 0.1840, 0.1288, 0.0925, 0.0527, 0.0318, 0.0125]
lmjm_krovetz_precision = [0.2819, 0.2439, 0.1931, 0.1397, 0.1000, 0.0821, 0.0520, 0.0375, 0.0232, 0.0133, 0.0000]
lmjm_none_precision = [0.2970, 0.2013, 0.1352, 0.0953, 0.0552, 0.0494, 0.0257, 0.0139, 0.0102, 0.0094, 0.0000]
# fmt: on

# Plot the un-interpolated mean average precision graph
plt.figure(figsize=(12, 8))
plt.plot(recall, bm25_porter_precision, marker="o", label="BM25 Porter")
plt.plot(recall, bm25_krovetz_precision, marker="o", label="BM25 Krovetz")
plt.plot(recall, bm25_none_precision, marker="o", label="BM25 None")
plt.plot(recall, lmmle_porter_precision, marker="o", label="LMMLE Porter")
plt.plot(recall, lmmle_krovetz_precision, marker="o", label="LMMLE Krovetz")
plt.plot(recall, lmmle_none_precision, marker="o", label="LMMLE None")
plt.plot(recall, lmjm_porter_precision, marker="o", label="LMJM Porter")
plt.plot(recall, lmjm_krovetz_precision, marker="o", label="LMJM Krovetz")
plt.plot(recall, lmjm_none_precision, marker="o", label="LMJM None")

# Customize
plt.title("Un-interpolated Mean Average Precision vs Recall")
plt.xlabel("Recall", fontsize=14)
plt.ylabel("Precision", fontsize=14)
plt.legend(loc="upper right", fontsize=10)
plt.grid(True, linestyle="--", alpha=0.6)
plt.xticks(recall)
plt.tight_layout()

# Display
plt.show()
