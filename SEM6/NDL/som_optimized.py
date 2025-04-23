import numpy as np
import matplotlib.pyplot as plt
from minisom import MiniSom

num_samples = 1000
input_dim = 3
data = np.random.random((num_samples, input_dim))

map_width, map_height = 10, 10
num_iterations = 2000

som = MiniSom(map_width, map_height, input_dim, sigma=1.0, learning_rate=0.5)
som.train_random(data, num_iterations)
som.random_weights_init(data)

weights = som.get_weights()

fig, ax = plt.subplots(figsize=(8, 8))
ax.set_title("Self-Organizing map")

plt.imshow(weights, interpolation='nearest')
plt.grid(False)
plt.show()
