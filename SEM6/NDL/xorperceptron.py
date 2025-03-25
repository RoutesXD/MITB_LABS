import numpy as np

# Sigmoid activation function and its derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# XOR dataset
inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
outputs = np.array([[0], [1], [1], [0]])  # Expected XOR outputs

# Initialize weights and biases
np.random.seed(0)  # For reproducibility
hidden_weights = np.random.uniform(-1, 1, (2, 2))  # 2 neurons in hidden layer
hidden_bias = np.random.uniform(-1, 1, (1, 2))
output_weights = np.random.uniform(-1, 1, (2, 1))  # 1 output neuron
output_bias = np.random.uniform(-1, 1, (1, 1))

# Hyperparameters
epochs = 10000
learning_rates = [0.01, 0.1, 0.5]  # Test different learning rates

# Train MLP for each learning rate
for lr in learning_rates:
    print(f"\nTraining with Learning Rate: {lr}")

    # Reinitialize weights for each learning rate
    hidden_weights = np.random.uniform(-1, 1, (2, 2))
    hidden_bias = np.random.uniform(-1, 1, (1, 2))
    output_weights = np.random.uniform(-1, 1, (2, 1))
    output_bias = np.random.uniform(-1, 1, (1, 1))

    for epoch in range(epochs):
        # Forward propagation
        hidden_layer_input = np.dot(inputs, hidden_weights) + hidden_bias
        hidden_layer_output = sigmoid(hidden_layer_input)

        output_layer_input = np.dot(hidden_layer_output, output_weights) + output_bias
        predicted_output = sigmoid(output_layer_input)

        # Calculate error
        error = outputs - predicted_output
        mean_squared_error = np.mean(np.square(error))

        # Backpropagation
        d_predicted_output = error * sigmoid_derivative(predicted_output)
        d_hidden_layer = np.dot(d_predicted_output, output_weights.T) * sigmoid_derivative(hidden_layer_output)

        # Update weights and biases
        output_weights += np.dot(hidden_layer_output.T, d_predicted_output) * lr
        output_bias += np.sum(d_predicted_output, axis=0, keepdims=True) * lr
        hidden_weights += np.dot(inputs.T, d_hidden_layer) * lr
        hidden_bias += np.sum(d_hidden_layer, axis=0, keepdims=True) * lr

        # Early stopping if error is minimal
        if mean_squared_error < 0.01:
            print(f"Stopped early at epoch {epoch + 1} with error: {mean_squared_error}")
            break

    # Final error
    print(f"Final Mean Squared Error: {mean_squared_error}")

    # Test the trained MLP
    print("\nXOR Gate Results:")
    for i in range(len(inputs)):
        hidden_layer_input = np.dot(inputs[i], hidden_weights) + hidden_bias
        hidden_layer_output = sigmoid(hidden_layer_input)

        output_layer_input = np.dot(hidden_layer_output, output_weights) + output_bias
        predicted_output = sigmoid(output_layer_input)

        print(f"Input: {inputs[i]} Predicted Output: {np.round(predicted_output[0], 2)}")
