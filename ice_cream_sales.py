import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = {
    "Temperature": [20, 25, 30, 35],
    "Ice Cream Sales": [50, 80, 120, 180]
}

df = pd.DataFrame(data)

X = df['Temperature'].values.reshape(-1,1)
y = df['Ice Cream Sales'].values

model = LinearRegression()
model.fit(X,y)

temp_to_predict = np.array([[40]])
predicted_sales = model.predict(temp_to_predict)

print("Estimated Ice Cream Sales at 40 degrees: {predicted_sales[0]:.2}")

plt.scatter(X,y, color='purple', label='Actual Data')
plt.plot(X, model.predict(X), color='red', label='Regression Line')
plt.title('Temperature vs Ice Cream Sales')
plt.xlabel('Temperature in Degrees Celcius')
plt.ylabel('Ice Cream Sales')
plt.legend()
plt.show() 