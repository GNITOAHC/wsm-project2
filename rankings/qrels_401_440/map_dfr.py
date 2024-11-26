import matplotlib.pyplot as plt

# Data for un-interpolated average precision across recall levels
# fmt: off
recall = [0.00, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 1.00]
bm25_porter_precision = [0.6626, 0.5298, 0.4591, 0.3644, 0.3149, 0.2582, 0.1820, 0.1220, 0.0584, 0.0222, 0.0137]
lmmle_porter_precision = [0.7444, 0.5406, 0.4651, 0.3713, 0.3293, 0.2672, 0.2009, 0.1627, 0.1021, 0.0658, 0.0319]
dfr_g_l_h2_precision = [0.5983, 0.4853, 0.4280, 0.3366, 0.2910, 0.2385, 0.1808, 0.1057, 0.0475, 0.0228, 0.0120]
dfr_ine_l_h2_precision = [0.5911, 0.4609, 0.3975, 0.3094, 0.2585, 0.2149, 0.1666, 0.0942, 0.0421, 0.0205, 0.0117]
dfr_in_l_h1_precision = [0.5940, 0.4554, 0.4120, 0.3180, 0.2576, 0.2065, 0.1460, 0.0768, 0.0394, 0.0159, 0.0109]
dfr_in_l_h2_precision = [0.6471, 0.5198, 0.4640, 0.3696, 0.3281, 0.2619, 0.1923, 0.1223, 0.0637, 0.0263, 0.0133]
dfr_in_l_h3_precision = [0.7378, 0.5615, 0.4796, 0.3752, 0.3145, 0.2561, 0.1774, 0.1206, 0.0538, 0.0175, 0.0084]
dfr_in_l_z_precision = [0.6752, 0.5405, 0.4670, 0.3892, 0.3366, 0.2930, 0.2253, 0.1745, 0.1323, 0.0731, 0.0321]
# fmt: on

# Plot the un-interpolated mean average precision graph
plt.figure(figsize=(12, 8))
plt.plot(recall, bm25_porter_precision, marker="o", label="BM25 Porter")
plt.plot(recall, lmmle_porter_precision, marker="o", label="LMMLE Porter")
plt.plot(recall, dfr_g_l_h2_precision, marker="o", label="DFR_G_L_H2")
plt.plot(recall, dfr_ine_l_h2_precision, marker="o", label="DFR_INE_L_H2")
plt.plot(recall, dfr_in_l_h1_precision, marker="o", label="DFR_IN_L_H1")
plt.plot(recall, dfr_in_l_h2_precision, marker="o", label="DFR_IN_L_H2")
plt.plot(recall, dfr_in_l_h3_precision, marker="o", label="DFR_IN_L_H3")
plt.plot(recall, dfr_in_l_z_precision, marker="o", label="DFR_IN_L_Z")


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
