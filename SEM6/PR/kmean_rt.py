import cv2
import numpy as np

cap = cv2.VideoCapture(0)
k = 4
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
attempts = 10

while True:
    ret, frame = cap.read()
    if not ret:
        break

    resized_frame = cv2.resize(frame, None, fx=0.5, fy=0.5)
    pixel_data = resized_frame.reshape((-1, 3))
    pixel_data = np.float32(pixel_data)

    _, labels, centers = cv2.kmeans(
        pixel_data, k, None, criteria, attempts, cv2.KMEANS_PP_CENTERS
    )

    centers = np.uint8(centers)
    segmented_data = centers[labels.flatten()]
    segmented_image = segmented_data.reshape(resized_frame.shape)

    cv2.imshow('Real-Time K-Means Clustering', segmented_image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
