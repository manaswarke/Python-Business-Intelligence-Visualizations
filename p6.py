import matplotlib.pyplot as plt
import pandas as pd

#data
data = pd.read_csv("IT products.csv")
products = data["products"]
sales = data["sales"]

plt.figure(figsize=(12,5))
bars = plt.bar(products, sales, width=0.3, color=["green"])
plt.xlabel("products", fontsize=16, color="red")
plt.ylabel("number of units sold", fontsize=16, color="blue")
plt.xticks(fontsize=12, color="red")
plt.yticks(fontsize=12, color="blue")
plt.title("Manas Warke", fontsize=20)
plt.bar_label(bars, fontsize=13, padding=3)
plt.show()