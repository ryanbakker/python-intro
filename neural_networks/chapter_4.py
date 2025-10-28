# Using the model to make predictions
from tensorflow import keras
import numpy as np

# Load data
data = keras.datasets.fashion_mnist
# Declare training and test data
(train_images, train_labels), (test_images, test_labels) = data.load_data()

# Get data labels
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# Reduce pixel size from up to 255, to be up to 1
train_images = train_images / 255.0
test_images = test_images / 255.0

# Define model architecture
model = keras.Sequential([
    # Flattened data input layer
    keras.Input(shape=(28, 28)),
    keras.layers.Flatten(),
    # Dense or fully connected hidden layer
    keras.layers.Dense(128, activation="relu"),
    # Fully connected output layer
    keras.layers.Dense(10, activation="softmax"),
])

# Set model parameters
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
# Train model with how many times it will train on the data (epochs)
model.fit(train_images, train_labels, epochs=7)

prediction = model.predict(test_images)

# Show results
for i in range(5):
    predicted_label = np.argmax(prediction[i])  # Find index of highest probability
    actual_label = test_labels[i]  # Actual class index

    print(f"Actual: {class_names[actual_label]} | Predicted: {class_names[predicted_label]}")
