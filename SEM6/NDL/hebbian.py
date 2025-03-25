# Implement the learning in neuron using Hebbian Learning algorithm

import numpy as np

class Neuron:
    def __init__(self, num_inputs):
        self.weights = np.random.rand(num_inputs)  # Initialize weights randomly
    
    def activate(self, inputs):
        # Compute the weighted sum of inputs
        weighted_sum = np.dot(inputs, self.weights)
        return weighted_sum
    
    def learn_hebbian(self, inputs, learning_rate):
        # Compute the activation
        activation = self.activate(inputs)
        
        # Update weights using Hebbian learning rule
        self.weights += learning_rate * activation * inputs

# Example usage
if __name__ == "__main__":
    # Create a neuron with 3 inputs
    num_inputs = 3
    neuron = Neuron(num_inputs)
    
    # Inputs for the neuron
    inputs = np.array([0.5, 0.3, 0.2])
    
    # Learning rate
    learning_rate = 0.1
    
    # Number of iterations for learning
    num_iterations = 1000
    
    # Learn using Hebbian learning algorithm
    for i in range(num_iterations):
        neuron.learn_hebbian(inputs, learning_rate)
    
    # Print the learned weights
    print("Learned weights:", neuron.weights)
