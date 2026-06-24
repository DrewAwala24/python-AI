#create dataset
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

data = {
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "Marks": [35, 45, 50, 60, 65, 75, 85, 95]
}

df = pd.DataFrame(data)
print(df)

#features(x),labels(y)
x = df[["Hours"]]
y = df["Marks"]

#Split Data
x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42
)

#Create model
model = LinearRegression()

#Train model
model.fit(x_train, y_train)

#output
LinearRegression()

#make predictions
predictions = model.predict(x_test)
print(predictions)

#predict new data
model.predict([[10]])

#visualize the model
plt.scatter(x, y)
plt.plot(x, model.predict(x), linewidth=2)
plt.title("Study Hours v Marks")
plt.xlabel("Hours")
plt.ylabel("Marks")
plt.show()

#evaluate model
mae = mean_absolute_error(y_test, predictions)
print(mae)

#calculate model accuracy
accuracy = model.score(x_test, y_test)
print(accuracy)