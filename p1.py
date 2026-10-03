import matplotlib.pyplot as plt


days = ["mon", "tue", "wed", "thu", "fri"]
visitors =[120, 150, 90, 180, 250]


plt.figure(figsize=(12,5))
plt.plot(days, visitors, linewidth=10, color="red", markersize=20, markerfacecolor="black")
plt.xlabel("Days", fontsize=16, fontweight="bold", color="red")
plt.ylabel("Number of visitors", fontsize=16, fontweight="bold", color="blue")
plt.title("Manas Warke's website")
plt.xticks(fontsize=14, color="red")
plt.yticks(fontsize=14, color="blue")
plt.grid()
plt.savefig("kc.pdf")
plt.savefig("kc.png")
plt.show()