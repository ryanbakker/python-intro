## Image loading options:

-1, cv2.IMREAD_COLOR = Loads a colour image, transparency will be neglected. This is the default flag.
0, cv2.IMREAD_GRAYSCALE = Loads image in grayscale mode
1, cv2.IMREAD_UNCHANGED = Loads original image including alpha channels (transparency)

## Color science:

- Typical image: RGB
- OpenCV uses: BGR

## Loading images:

When images are loaded in with CV they are extracted into a numpy array dividing the images
pixels into an array of rows, then in each row an array of columns, with each array element being a
BGR value ([128, 255, 92]).


