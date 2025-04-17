import numpy as np
import matplotlib.pyplot as plt

class HopfieldNetwork:
    def __init__(self, size):
        self.size = size
        self.weights = np.zeros((size, size))

    def train(self, patterns):
        for p in patterns:
            p = p.reshape(self.size, 1)
            self.weights += np.dot(p, p.T)
        np.fill_diagonal(self.weights, 0)

    def recall(self, pattern, steps=5):
        pattern = pattern.copy()
        for _ in range(steps):
            for i in range(self.size):
                raw_input = np.dot(self.weights[i], pattern)
                pattern[i] = 1 if raw_input >= 0 else -1
        return pattern

def print_pattern(p, shape):
    p = p.reshape(shape)
    for row in p:
        print(''.join(['⬛' if val == 1 else '⬜' for val in row]))
    print()

pattern_A = np.array([
    -1,  1,  1,  1, -1,
     1, -1, -1, -1,  1,
     1,  1,  1,  1,  1,
     1, -1, -1, -1,  1,
     1, -1, -1, -1,  1
])

pattern_B = np.array([
     1,  1,  1,  1, -1,
     1, -1, -1, -1, -1,
     1,  1,  1,  1, -1,
     1, -1, -1, -1, -1,
     1,  1,  1,  1, -1
])

network = HopfieldNetwork(size=25)
network.train([pattern_A, pattern_B])

noisy_A = pattern_A.copy()
noisy_A[3] = -1
noisy_A[6] = 1

print("Noisy Input:")
print_pattern(noisy_A, (5, 5))

recalled = network.recall(noisy_A)
print("Recalled Pattern:")
print_pattern(recalled, (5, 5))
