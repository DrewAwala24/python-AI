import pandas as pd
import numpy as np

data = {
    "Product": ["Sugar", "Bread", "Milk", "Rice"],
    "Sales": [150, 200, 180, 220]
}
df = pd.DataFrame(data)
print(df)

total = np.sum(df["Sales"])
print("Total Sales:",total) 

average = np.mean(df["Sales"])
print("Average Sales:",average)

highest_sales = (df.loc[df["Sales"].idxmax()])
print("Prod with highest sales:",highest_sales)