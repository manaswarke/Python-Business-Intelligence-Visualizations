import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("sales.csv")
print(data)
months = data["months"]
online = data["online"]
offline = data["offline"]

x = np.arange(len(months))
plt.figure(figsize=(14,6))
b1 = plt.bar(x-0.16, online, width=0.30, color="pink", label="online")
b2 = plt.bar(x+0.16, offline, width = 0.30, color="purple", label="oflfine")
plt.bar_label(b1, fontsize=13, padding=3)
plt.bar_label(b2, fontsize=13, padding=3)
plt.xticks(x, months)
plt.legend(fontsize=14, shadow = True)
plt.show()