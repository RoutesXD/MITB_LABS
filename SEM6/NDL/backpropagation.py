import numpy as np

class RecurrentNeuralNetwork:
    def __init__(self, input_dim, hidden_dim, output_dim, learning_rate=0.001, time_steps=5):
        self.input_dim = input_dim
        self.hidden_dim = hidden_dim
        self.output_dim = output_dim
        self.learning_rate = learning_rate
        self.time_steps = time_steps

        # Initialize weights with smaller values to avoid instability
        self.Wxh = np.random.randn(hidden_dim, input_dim) * 0.01  # Input to hidden
        self.Whh = np.random.randn(hidden_dim, hidden_dim) * 0.01  # Hidden to hidden (recurrent)
        self.Why = np.random.randn(output_dim, hidden_dim) * 0.01  # Hidden to output
        self.bh = np.zeros((hidden_dim, 1))
        self.by = np.zeros((output_dim, 1))

    def forward(self, inputs):
        """Forward pass through time."""
        h = np.zeros((self.hidden_dim, 1))  # Initial hidden state
        self.h_states = { -1: h }
        self.outputs = {}

        for t in range(self.time_steps):
            h = np.tanh(np.dot(self.Wxh, inputs[t]) + np.dot(self.Whh, self.h_states[t-1]) + self.bh)
            y = np.dot(self.Why, h) + self.by
            self.h_states[t] = h
            self.outputs[t] = y

        return self.outputs

    def backward(self, inputs, targets):
        """Backward pass using Backpropagation Through Time (BPTT)."""
        dWxh, dWhh, dWhy = np.zeros_like(self.Wxh), np.zeros_like(self.Whh), np.zeros_like(self.Why)
        dbh, dby = np.zeros_like(self.bh), np.zeros_like(self.by)
        dh_next = np.zeros((self.hidden_dim, 1))

        for t in reversed(range(self.time_steps)):
            dy = self.outputs[t] - targets[t]
            dWhy += np.dot(dy, self.h_states[t].T)
            dby += dy

            dh = np.dot(self.Why.T, dy) + dh_next
            dh_raw = (1 - self.h_states[t] ** 2) * dh  # Derivative of tanh
            dbh += dh_raw
            dWxh += np.dot(dh_raw, inputs[t].T)
            dWhh += np.dot(dh_raw, self.h_states[t-1].T)
            dh_next = np.dot(self.Whh.T, dh_raw)

        # Gradient Clipping to avoid exploding gradients
        for dparam in [dWxh, dWhh, dWhy, dbh, dby]:
            np.clip(dparam, -5, 5, out=dparam)

        # Update weights
        for param, dparam in zip([self.Wxh, self.Whh, self.Why, self.bh, self.by], [dWxh, dWhh, dWhy, dbh, dby]):
            param -= self.learning_rate * dparam

    def train(self, data, labels, epochs=100):
        """Train the network over multiple epochs."""
        for epoch in range(epochs):
            loss = 0
            for inputs, targets in zip(data, labels):
                outputs = self.forward(inputs)
                self.backward(inputs, targets)
                loss += np.sum((outputs[self.time_steps-1] - targets[self.time_steps-1])**2) / 2

            if epoch % 10 == 0:
                print(f"Epoch {epoch}, Loss: {loss:.4f}")

# Example usage
if __name__ == "__main__":
    time_steps = 5
    input_dim = 3
    hidden_dim = 4
    output_dim = 2

    # Normalize input data to stabilize training
    data = [np.random.randn(time_steps, input_dim, 1) * 0.1 for _ in range(100)]
    labels = [np.random.randn(time_steps, output_dim, 1) * 0.1 for _ in range(100)]

    rnn = RecurrentNeuralNetwork(input_dim, hidden_dim, output_dim)
    rnn.train(data, labels, epochs=50)