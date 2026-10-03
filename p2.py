import matplotlib.pyplot as plt
import pandas as pd

#data
data = pd.read_csv("kc.csv")
days = data["days"]
visitors = data["visitors"]

#code
plt.figure(figsize=(12,5))
plt.plot(days, visitors, linewidth=10, color="red", marker="o", markersize=20, markerfacecolor="black")
plt.xlabel("Days", fontsize=16, fontweight="bold", color="red")
plt.ylabel("Number of visitors", fontsize=16, fontweight="bold", color="blue")
plt.title("Manas Warke's website")
plt.xticks(fontsize=14, color="red")
plt.yticks(fontsize=14, color="blue")
plt.grid()
plt.savefig("kc.pdf")
plt.savefig("kc.png")
plt.show()