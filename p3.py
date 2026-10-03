import matplotlib.pyplot as plt
import pandas as pd

#data
data = pd.read_csv("website.csv")
weeks = data["weeks"]
organic = data["organic"]
social = data["social"]
ads = data["ads"]

plt.plot(weeks, organic)
plt.plot(weeks,social)
plt.plot(weeks, ads)

#code
plt.figure(figsize=(14,5))
plt.plot(weeks,organic,linewidth=7, marker="o", markersize=15, markerfacecolor="black", label="organic")
plt.plot(weeks,social,linewidth=7, marker="s", markersize=15, markerfacecolor="black", label="social")
plt.plot(weeks,ads,linewidth=7, marker="p", markersize=15, markerfacecolor="black", label="ads")
plt.xlabel("Weeks", fontsize=14, fontweight="bold", color="red")
plt.ylabel("Number of visitors", fontsize=14, fontweight="bold", color="blue")
plt.xticks(color="red")
plt.yticks(color="blue")
plt.grid()
plt.legend(fontsize=16, shadow=True)
plt.show()

