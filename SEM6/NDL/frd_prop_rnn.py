import numpy as np

def rnn_forward(X, h0, W_x, W_h, b_h, W_y, b_y):
    """
    Perform forward propagation for an entire sequence.

    Arguments:
    X    -- input data for every time-step (shape: time_steps, input_size)
    h0   -- initial hidden state (shape: hidden_size, 1)
    W_x  -- Weight matrix for input (shape: hidden_size, input_size)
    W_h  -- Weight matrix for hidden state (shape: hidden_size, hidden_size)
    b_h  -- Bias vector for hidden state (shape: hidden_size, 1)
    W_y  -- Weight matrix for output (shape: output_size, hidden_size)
    b_y  -- Bias vector for output (shape: output_size, 1)

    Returns:
    h -- Hidden states for every time-step
    y -- Outputs for every time-step
    """
    time_steps = X.shape[0]
    hidden_size = h0.shape[0]
    output_size = W_y.shape[0]

    h = np.zeros((time_steps, hidden_size, 1))  # Store all hidden states
    y = np.zeros((time_steps, output_size, 1))  # Store all outputs

    h_prev = h0

    for t in range(time_steps):
        x_t = X[t].reshape(-1, 1)  # Input at time t (shape: input_size, 1)
        h_t = np.tanh(np.dot(W_x, x_t) + np.dot(W_h, h_prev) + b_h)
        y_t = np.dot(W_y, h_t) + b_y

        h[t] = h_t
        y[t] = y_t
        h_prev = h_t  # Update hidden state for next time step

    return h, y


# Example dimensions
time_steps = 4
input_size = 3
hidden_size = 5
output_size = 2

# Random initializations
np.random.seed(1)
X = np.random.randn(time_steps, input_size)  # Inputs for 4 time steps
h0 = np.zeros((hidden_size, 1))              # Initial hidden state
W_x = np.random.randn(hidden_size, input_size)
W_h = np.random.randn(hidden_size, hidden_size)
b_h = np.random.randn(hidden_size, 1)
W_y = np.random.randn(output_size, hidden_size)
b_y = np.random.randn(output_size, 1)

# Perform full forward propagation
h, y = rnn_forward(X, h0, W_x, W_h, b_h, W_y, b_y)

print("Hidden states:\n", h)
print("\nOutputs:\n", y)
