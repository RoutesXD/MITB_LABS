import numpy as np

def step_function(x):
    return 1 if x >= 0 else 0

def perceptron_learning(X, y, learning_rate=0.1, epochs=10):
    weights = np.zeros(X.shape[1])
    bias = 0
    for epoch in range(epochs):
        for i in range(len(X)):
            linear_output = np.dot(X[i], weights) + bias
            prediction = step_function(linear_output)
            error = y[i] - prediction
            weights += learning_rate * error * X[i]
            bias += learning_rate * error
    return weights, bias

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 0, 0, 1])

weights, bias = perceptron_learning(X, y)

def predict(X, weights, bias):
    linear_output = np.dot(X, weights) + bias
    return step_function(linear_output)

for x in X:
    print(f"Input: {x}, Predicted Output: {predict(x, weights, bias)}")
