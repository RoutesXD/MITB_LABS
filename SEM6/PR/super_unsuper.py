import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical
 
# Load images from directory
def load_images_from_folder(folder, img_size=(64, 64)):
    images = []
    labels = []
    class_names = os.listdir(folder)
    
    for label, class_name in enumerate(class_names):
        class_path = os.path.join(folder, class_name)
        if not os.path.isdir(class_path):
            continue
        for file in os.listdir(class_path):
            img_path = os.path.join(class_path, file)
            img = cv2.imread(img_path)
            if img is not None:
                img = cv2.resize(img, img_size)
                img = img / 255.0  # Normalize
                images.append(img)
                labels.append(label)
    
    return np.array(images), np.array(labels), class_names
 
# Load dataset
folder_path = "path_to_your_images"
X, y, class_names = load_images_from_folder(folder_path)
 
# Split into training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
 
# One-hot encoding labels for supervised learning
y_train_cat = to_categorical(y_train, num_classes=len(class_names))
y_test_cat = to_categorical(y_test, num_classes=len(class_names))
 
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
 
# Build CNN Model
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(64, 64, 3)),
    MaxPooling2D(pool_size=(2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(pool_size=(2, 2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(len(class_names), activation='softmax')
])
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
 # Train the model
model.fit(X_train, y_train_cat, epochs=10, validation_data=(X_test, y_test_cat), batch_size=32)
# Evaluate the model
test_loss, test_acc = model.evaluate(X_test, y_test_cat)
print(f"Test Accuracy: {test_acc:.2f}")
from sklearn.cluster import KMeans
 # Flatten images for clustering
X_flattened = X.reshape(X.shape[0], -1)
# Apply K-Means
k = len(class_names)  # Number of clusters (same as number of classes)
kmeans = KMeans(n_clusters=k, random_state=42)
labels = kmeans.fit_predict(X_flattened)
 
# Plot some clustered images
fig, axes = plt.subplots(1, 5, figsize=(10, 5))
for i, ax in enumerate(axes):
    ax.imshow(X[i])
    ax.set_title(f"Cluster {labels[i]}")
    ax.axis('off')
plt.show()
