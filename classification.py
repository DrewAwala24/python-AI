import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

iris = load_iris()
print(iris.feature_names)
print(iris.target_names)

df = pd.DataFrame(data=iris.data, columns = iris.feature_names)
print(df.head())

X = iris.data
y = iris.target

model = RandomForestClassifier()
model.fit(X,y)

predictions = model.predict([[5.1, 3.5, 1.4, 0.2]])
print(predictions)
print(iris.target_names[predictions])
