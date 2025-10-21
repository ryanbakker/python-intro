import cv2
import random

# Load image
img = cv2.imread('assets/logo.jpg', -1)

# Get the first 100 rows of the image and for each column, replace BGR colors with random values
for i in range(100):
    for j in range(img.shape[1]):
        img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

# Copy part of the image and paste it somewhere else
# Copy rows 500 to 700, and in those rows; columns 600 to 900
tag = img[500:700, 600:900]
# Take the copy section and move it to 100:300, and scale up to 650:950
img[100:300, 650: 950] = tag

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
