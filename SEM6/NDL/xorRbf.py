import numpy as np
import matplotlib.pyplot as plt

inputs = np.array([[0,0], [0,1], [1,0], [1,1]])
outputs = np.array([0, 1, 1, 0])

def gaussian(vector, weights):
    return np.exp(-np.linalg.norm(vector - weights)**2)

w1 = np.array([1, 1])
w2 = np.array([0, 0])

f1, f2 = [], []

print("Input First Function Second Function")
for i in inputs:
    v1, v2 = gaussian(i, w1), gaussian(i, w2)
    f1.append(v1)
    f2.append(v2)
    print(f"{i} {v1:.4f} {v2:.4f}")

f1, f2 = [], []

inputs = np.array([[0,0], [1,1], [0,1], [1,0]])
outputs = np.array([0, 0, 1, 1])

for i in inputs:
    v1, v2 = gaussian(i, w1), gaussian(i, w2)
    f1.append(v1)
    f2.append(v2)

fig, ax = plt.subplots(figsize=(4, 4))
ax.scatter(f1[2:], f2[2:], marker="x", label="Hidden Function 1")
ax.scatter(f1[:2], f2[:2], marker="o", label="Hidden Function 2")

plt.xlabel("$warphi_1$")
plt.ylabel("$warphi_2$")

x = np.linspace(0, 1, 10)
y = x + 1
ax.plot(x, y, label="y = x + 0.8")
ax.set_xlim(left=-0.1)
ax.set_ylim(bottom=-0.1)

plt.show()