import matplotlib.pyplot as plt

# Data for un-interpolated average precision across recall levels
# fmt: off
recall = [0.00, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 1.00]
bm25_porter_precision = [0.6141, 0.5372, 0.4281, 0.3765, 0.2997, 0.2767, 0.2027, 0.1595, 0.0756, 0.0181, 0.0033]
bm25_krovetz_precision = [0.2284, 0.2054, 0.1672, 0.1239, 0.0881, 0.0823, 0.0736, 0.0531, 0.0168, 0.0000, 0.0000]
bm25_none_precision = [0.1430, 0.1151, 0.0735, 0.0627, 0.0610, 0.0607, 0.0562, 0.0538, 0.0171, 0.0000, 0.0000]
lmmle_porter_precision = [0.5247, 0.4304, 0.3524, 0.3310, 0.2925, 0.2629, 0.2168, 0.1625, 0.1391, 0.1154, 0.0475]
lmmle_krovetz_precision = [0.1545, 0.1461, 0.1249, 0.1031, 0.0772, 0.0742, 0.0735, 0.0708, 0.0587, 0.0293, 0.0167]
lmmle_none_precision = [0.1243, 0.1112, 0.0664, 0.0617, 0.0601, 0.0589, 0.0589, 0.0589, 0.0479, 0.0241, 0.0164]
lmjm_porter_precision = [0.5824, 0.4251, 0.3402, 0.3116, 0.2654, 0.1999, 0.1732, 0.1307, 0.0842, 0.0371, 0.0061]
lmjm_krovetz_precision = [0.2087, 0.1483, 0.1291, 0.0935, 0.0815, 0.0797, 0.0721, 0.0581, 0.0250, 0.0059, 0.0000]
lmjm_none_precision = [0.0956, 0.0949, 0.0620, 0.0606, 0.0594, 0.0579, 0.0529, 0.0513, 0.0230, 0.0040, 0.0000]
dfr_in_l_h3_porter_precision = [0.6011, 0.5496, 0.4509, 0.3819, 0.2780, 0.2376, 0.1551, 0.0955, 0.0606, 0.0178, 0.0025]
dfr_in_l_z_porter_precision = [0.6752, 0.5405, 0.4670, 0.3892, 0.3366, 0.2930, 0.2253, 0.1745, 0.1323, 0.0731, 0.0321]
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
plt.plot(recall, dfr_in_l_h3_porter_precision, marker="o", label="DFR In L H3 Porter")
plt.plot(recall, dfr_in_l_z_porter_precision, marker="o", label="DFR In L Z Porter")

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
