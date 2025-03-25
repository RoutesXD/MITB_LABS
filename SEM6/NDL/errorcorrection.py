import numpy as np

class Neuron:
    def __init__(self, num_inputs):
        self.weights = np.random.rand(num_inputs)  # Initialize weights randomly
        self.bias = np.random.rand()  # Initialize bias randomly

    def activate(self, inputs):
        # Compute the weighted sum of inputs and bias
        weighted_sum = np.dot(inputs, self.weights) + self.bias
        # Apply activation function (sigmoid)
        activation = self.sigmoid(weighted_sum)
        return activation

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def train(self, inputs, target_output, learning_rate):
        # Compute the actual output
        actual_output = self.activate(inputs)
        
        # Compute the error
        error = target_output - actual_output

        # Update weights and bias based on the error
        self.weights += learning_rate * error * inputs
        self.bias += learning_rate * error

# Example usage
if __name__ == "__main__":
    # Create a neuron with 3 inputs
    num_inputs = 3
    neuron = Neuron(num_inputs)

    # Training data
    X_train = np.array([[0, 0, 1], 
                         [1, 1, 1], 
                         [1, 0, 1], 
                         [0, 1, 1]])
    y_train = np.array([0, 1, 1, 0])

    # Learning rate
    learning_rate = 0.1

    # Number of iterations for learning
    num_iterations = 10000

    # Train the neuron
    for i in range(num_iterations):
        # Randomly select a training example
        index = np.random.randint(len(X_train))
        inputs = X_train[index]
        target_output = y_train[index]
        neuron.train(inputs, target_output, learning_rate)

    # Test the trained neuron
    test_data = np.array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
    for inputs in test_data:
        output = neuron.activate(inputs)
        print("Input:", inputs, "Output:", output)
