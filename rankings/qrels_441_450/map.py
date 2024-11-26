import matplotlib.pyplot as plt

# fmt: off
recall = [0.00, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 1.00]
porter_model = [0.3022, 0.2079, 0.1713, 0.1444, 0.1113, 0.0883, 0.0736, 0.0626, 0.0471, 0.0253, 0.0083]
combination_model = [0.2217, 0.2120, 0.1672, 0.1309, 0.0968, 0.0786, 0.0653, 0.0405, 0.0180, 0.0120, 0.0047]
top2_model = [0.3695, 0.2378, 0.1297, 0.1131, 0.0899, 0.0598, 0.0455, 0.0378, 0.0328, 0.0213, 0.0000]
porter_minmax_model = [0.3766, 0.2436, 0.1780, 0.1587, 0.1520, 0.1132, 0.0993, 0.0625, 0.0493, 0.0318, 0.0097]
porter_robust_model = [0.4917, 0.3679, 0.3144, 0.2391, 0.1541, 0.1219, 0.1090, 0.0856, 0.0682, 0.0500, 0.0270]
porter_with_dfrh3_r_model = [0.5271, 0.4143, 0.3371, 0.2471, 0.1927, 0.1456, 0.1076, 0.0882, 0.0633, 0.0384, 0.0114]
porter_with_dfrh3_m_model = [0.3578, 0.3130, 0.1866, 0.1716, 0.1640, 0.1424, 0.1196, 0.0820, 0.0601, 0.0403, 0.0046]
porter_with_dfrh3_model = [0.2151, 0.1921, 0.1611, 0.1370, 0.1179, 0.1001, 0.0737, 0.0627, 0.0424, 0.0300, 0.0000]
# fmt: on

# Plot the un-interpolated mean average precision graph
plt.figure(figsize=(12, 8))
plt.plot(recall, porter_model, marker="o", label="PorterModel")
plt.plot(recall, combination_model, marker="o", label="CombinationModel")
plt.plot(recall, top2_model, marker="o", label="Top2Model")
plt.plot(recall, porter_minmax_model, marker="o", label="PorterMinMaxModel")
plt.plot(recall, porter_robust_model, marker="o", label="PorterRobustModel")
plt.plot(recall, porter_with_dfrh3_r_model, marker="o", label="PorterWithDfrModel_R")
plt.plot(recall, porter_with_dfrh3_m_model, marker="o", label="PorterWithDfrModel_M")
plt.plot(recall, porter_with_dfrh3_model, marker="o", label="PorterWithDfrModel")

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
