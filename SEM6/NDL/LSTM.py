import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def lstm_cell_forward(x_t, h_prev, c_prev, parameters):
    """
    Implements a single forward step of the LSTM cell.

    Arguments:
    x_t -- input data at time step t (shape: input_size, 1)
    h_prev -- hidden state at time step t-1 (shape: hidden_size, 1)
    c_prev -- memory state at time step t-1 (shape: hidden_size, 1)
    parameters -- python dictionary containing:
        W_f, b_f -- forget gate parameters
        W_i, b_i -- input gate parameters
        W_c, b_c -- candidate memory parameters
        W_o, b_o -- output gate parameters

    Returns:
    h_next -- next hidden state
    c_next -- next memory state
    """

    # Retrieve parameters
    W_f = parameters["W_f"]
    b_f = parameters["b_f"]
    W_i = parameters["W_i"]
    b_i = parameters["b_i"]
    W_c = parameters["W_c"]
    b_c = parameters["b_c"]
    W_o = parameters["W_o"]
    b_o = parameters["b_o"]

    # Concatenate h_prev and x_t
    concat = np.vstack((h_prev, x_t))

    # Forget gate
    f_t = sigmoid(np.dot(W_f, concat) + b_f)

    # Input gate
    i_t = sigmoid(np.dot(W_i, concat) + b_i)

    # Candidate memory
    c_tilde = np.tanh(np.dot(W_c, concat) + b_c)

    # Update cell state
    c_next = f_t * c_prev + i_t * c_tilde

    # Output gate
    o_t = sigmoid(np.dot(W_o, concat) + b_o)

    # Next hidden state
    h_next = o_t * np.tanh(c_next)

    return h_next, c_next

# ---------------------- Example Usage ----------------------

np.random.seed(2)

input_size = 3
hidden_size = 5

x_t = np.random.randn(input_size, 1)       # Current input
h_prev = np.random.randn(hidden_size, 1)   # Previous hidden state
c_prev = np.random.randn(hidden_size, 1)   # Previous cell state

# Random weight and bias initialization
parameters = {
    "W_f": np.random.randn(hidden_size, hidden_size + input_size),
    "b_f": np.random.randn(hidden_size, 1),
    "W_i": np.random.randn(hidden_size, hidden_size + input_size),
    "b_i": np.random.randn(hidden_size, 1),
    "W_c": np.random.randn(hidden_size, hidden_size + input_size),
    "b_c": np.random.randn(hidden_size, 1),
    "W_o": np.random.randn(hidden_size, hidden_size + input_size),
    "b_o": np.random.randn(hidden_size, 1),
}

# Perform a single LSTM step
h_next, c_next = lstm_cell_forward(x_t, h_prev, c_prev, parameters)

print("Next hidden state h_next:\n", h_next)
print("\nNext cell state c_next:\n", c_next)
