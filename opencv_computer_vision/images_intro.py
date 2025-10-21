import cv2

# Load image
img = cv2.imread('assets/logo.jpg', 1)
# Resize image to half its width and height
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
# Rotate image
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

# Save img as new image to project directory
cv2.imwrite('assets/new_logo.jpg', img)

# Show image
cv2.imshow('Image', img)
# Wait here until a key is pressed to continue
cv2.waitKey(0)
# Close window
cv2.destroyAllWindows()
