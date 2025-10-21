import numpy as np
import cv2

# Load device camera 0 (webcam - first camera)
cap = cv2.VideoCapture(0)

while True:
    # Return image frame
    ret, frame = cap.read()
    # Get webcam frame width & height
    width = int(cap.get(3))
    height = int(cap.get(4))

    image = np.zeros(frame.shape, np.uint8)
    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    # Top left
    image[:height // 2, :width // 2] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
    # Bottom left
    image[height // 2:, :width // 2] = smaller_frame
    # Top right
    image[:height // 2, width // 2:] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
    # Bottom right
    image[height // 2:, width // 2:] = smaller_frame

    # Display frame
    cv2.imshow('frame', image)

    # Wait 1ms and break on pressing q
    if cv2.waitKey(1) == ord('q'):
        break

# Release camera resource for other software to use
cap.release()
cv2.destroyAllWindows()
