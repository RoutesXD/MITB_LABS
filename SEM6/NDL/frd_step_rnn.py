import numpy as np

def rnn_cell_forward(x_t, h_prev, W_x, W_h, b):
    """
    Single forward step of a basic RNN cell.

    Arguments:
    x_t -- input at time step t (shape: input_size, 1)
    h_prev -- hidden state at time step t-1 (shape: hidden_size, 1)
    W_x -- Weight matrix for input (shape: hidden_size, input_size)
    W_h -- Weight matrix for hidden state (shape: hidden_size, hidden_size)
    b -- Bias vector (shape: hidden_size, 1)

    Returns:
    h_t -- next hidden state (shape: hidden_size, 1)
    """
    h_t = np.tanh(np.dot(W_x, x_t) + np.dot(W_h, h_prev) + b)
    return h_t

# Example dimensions
input_size = 3
hidden_size = 5

# Random initializations
np.random.seed(1)
x_t = np.random.randn(input_size, 1)           # Input at time t
h_prev = np.random.randn(hidden_size, 1)       # Previous hidden state
W_x = np.random.randn(hidden_size, input_size) # Input weights
W_h = np.random.randn(hidden_size, hidden_size) # Hidden weights
b = np.random.randn(hidden_size, 1)            # Bias

# Perform a single forward step
h_t = rnn_cell_forward(x_t, h_prev, W_x, W_h, b)
print("Next hidden state h_t:\n", h_t)
