import numpy as np

def train_hopfield(patterns):
    """Train a Hopfield network using the Hebbian learning rule."""
    num_neurons = len(patterns[0])
    weight_matrix = np.zeros((num_neurons, num_neurons))
    
    for pattern in patterns:
        pattern = np.array(pattern).reshape(-1, 1)
        weight_matrix += pattern @ pattern.T
    
    np.fill_diagonal(weight_matrix, 0)  # No self-connections
    return weight_matrix

def recall_pattern(weight_matrix, input_pattern, max_iterations=10):
    """Recall a pattern using the trained Hopfield network."""
    output_pattern = np.array(input_pattern)

    for _ in range(max_iterations):
        for i in range(len(output_pattern)):
            net_input = np.dot(weight_matrix[i], output_pattern)
            output_pattern[i] = 1 if net_input >= 0 else -1
            
    return output_pattern

# Original pattern
original_pattern = [-1, 1, -1, -1, -1, -1, -1, 1, -1, 1]

# Train the Hopfield network
weight_matrix = train_hopfield([original_pattern])

# Noisy pattern to recover
noisy_pattern = [-1, -1, -1, 1, -1, -1, -1, 1, -1, -1]

# Recovered pattern
recovered_pattern = recall_pattern(weight_matrix, noisy_pattern)

print("Original Pattern:", original_pattern)
print("Noisy Pattern:", noisy_pattern)
print("Recovered Pattern:", recovered_pattern)
