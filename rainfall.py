import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("transnzoiarainfall.csv")
df = pd.DataFrame(data)
print(df.head())

average = np.mean(df["Rainfall_mm"])
print("Average Rainfall: ",average)

x = df["Month"]
y = df["Rainfall_mm"]
plt.bar(x,y)
plt.title("Rainfall in Trans Nzoia")
plt.xlabel("Months")
plt.ylabel("Rainfall_mm")
plt.show