import numpy as np
import matplotlib.pyplot as plt

# Input range
x = np.linspace(-10, 10, 1000)

# Activation functions
def binary_step(x):
    return np.where(x >= 0, 1, 0)

def linear(x):
    return x

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def tanh(x):
    return np.tanh(x)

def relu(x):
    return np.maximum(0, x)

def leaky_relu(x, alpha=0.01):
    return np.where(x > 0, x, alpha * x)

def softmax(x):
    exp_x = np.exp(x - np.max(x))  # For numerical stability
    return exp_x / exp_x.sum()

# Plotting
plt.figure(figsize=(12, 10))

activations = {
    'Binary Step': binary_step(x),
    'Linear': linear(x),
    'Sigmoid': sigmoid(x),
    'Tanh': tanh(x),
    'ReLU': relu(x),
    'Leaky ReLU': leaky_relu(x),
    'Softmax': softmax(x)  # Softmax applied to vector
}

for i, (name, y) in enumerate(activations.items(), 1):
    plt.subplot(4, 2, i)
    plt.plot(x, y)
    plt.title(name)
    plt.grid(True)
    plt.ylim(-1.5, 1.5 if name != 'Softmax' else np.max(y) + 0.1)

plt.tight_layout()
plt.show()
