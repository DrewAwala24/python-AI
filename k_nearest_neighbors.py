from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Load the Iris dataset as a pandas DataFrame (features + target)
iris = load_iris(as_frame=True)
print(iris)

# Select two features (sepal length and sepal width) for a simple 2D example
X = iris.data[["sepal length (cm)", "sepal width (cm)"]]

# Set the target variable (species labels)
y = iris.target

# Split the dataset into training and test sets.
# `stratify=y` preserves class proportions; `random_state` ensures reproducibility.
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=0)

# Create the K-Nearest Neighbors classifier with k=3 neighbors
model = KNeighborsClassifier(n_neighbors=3)

# Train the model on the training data (fit the classifier)
model.fit(X_train, y_train)

print("Accuracy Score: ",model.score(X_test, y_test))  # Evaluate the model on the test set and print the accuracy score
print(model.predict(X_test))  # Predict the classes for the test set and print the predicted labels

print("Prediction for [SP = 3.0, SW = 3.0]: ", model.predict([[3.0, 3.0]]))