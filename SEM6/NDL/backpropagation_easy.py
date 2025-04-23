import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt 

x_train = np.random.random((1000, 10, 5))
y_train = np.sum(x_train, axis=(1, 2))

model = tf.keras.Sequential([ 
    tf.keras.layers.SimpleRNN(16, input_shape=(10, 5)), 
    tf.keras.layers.Dense(1) 
])

model.compile(optimizer='adam', loss='mse')

history = model.fit(x_train, y_train, epochs=50)

plt.plot(history.history['loss'], label='loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.title('Training Loss')
plt.legend()
plt.show()
