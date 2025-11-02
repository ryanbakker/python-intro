from tensorflow import keras
import numpy as np

# ===============================
# Load and Prepare the IMDB Dataset
# ===============================

# Load IMDB reviews dataset (only keep the 88,000 most frequent words)
data = keras.datasets.imdb
(train_data, train_labels), (test_data, test_labels) = data.load_data(num_words=88000)

# Convert words to integers (and shift by +3 for special tokens)
word_index = data.get_word_index()
word_index = {k: (v + 3) for k, v in word_index.items()}

# Add special tokens to the index
word_index["<PAD>"] = 0  # Padding token (used to make all reviews same length)
word_index["<START>"] = 1  # Indicates start of a review
word_index["<UNK>"] = 2  # Unknown word (not in dictionary)
word_index["<UNUSED>"] = 3  # Placeholder for unused words

# Reverse the mapping so we can decode integers back into words
reverse_word_index = dict([(value, key) for (key, value) in word_index.items()])

# Make sure all reviews are the same length by padding or cutting to 250 words
train_data = keras.preprocessing.sequence.pad_sequences(
    train_data, value=word_index["<PAD>"], padding="post", maxlen=250
)
test_data = keras.preprocessing.sequence.pad_sequences(
    test_data, value=word_index["<PAD>"], padding="post", maxlen=250
)


# Decode integer-encoded reviews back into readable text
def decode_review(text):
    return " ".join([reverse_word_index.get(i, "?") for i in text])


# ===============================
# Define the Model Architecture
# ===============================

def build_model():
    # Sequential model: layer-by-layer structure
    model = keras.Sequential([
        # Converts integer-encoded words into dense 16-dimensional vectors
        keras.layers.Embedding(88000, 16),

        # Averages the word embeddings so each review becomes a single vector
        keras.layers.GlobalAveragePooling1D(),

        # Hidden layer with 16 neurons and ReLU activation
        keras.layers.Dense(16, activation="relu"),

        # Output layer: one neuron with sigmoid activation (0 = negative, 1 = positive)
        keras.layers.Dense(1, activation="sigmoid")
    ])

    # Compile model with optimizer, loss function, and accuracy metric
    model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
    return model


# ===============================
# Train Multiple Times and Save the Best Model
# ===============================

best_acc = 0.0  # Track best validation accuracy across runs
best_model = None  # Store the best performing model

# Split off part of the training data for validation
x_val = train_data[:10000]
x_train = train_data[10000:]
y_val = train_labels[:10000]
y_train = train_labels[10000:]

# Train the model 5 times, each with 15 epochs
for i in range(5):
    print(f"\n--- Training Run {i + 1}/5 ---")

    # Build a fresh model for each run
    model = build_model()

    # Train the model and record its progress
    history = model.fit(
        x_train, y_train,
        epochs=15,  # Number of times the model sees all training data
        batch_size=512,  # Number of samples processed at a time
        validation_data=(x_val, y_val),
        verbose=1
    )

    # Track the best validation accuracy achieved in this run
    val_acc = max(history.history["val_accuracy"])
    print(f"Run {i + 1} - Best Validation Accuracy: {val_acc:.4f}")

    # If this model performed better than previous runs, save it
    if val_acc > best_acc:
        best_acc = val_acc
        best_model = model
        best_model.save("model.keras")
        print(f"New best model saved with accuracy {best_acc:.4f}")

print(f"\nTraining complete. Best validation accuracy: {best_acc:.4f}")
print("Best model saved as model.keras")

# ===============================
# Evaluate the Best Model
# ===============================

# Load the saved best model from disk
loaded_model = keras.models.load_model("model.keras")

# Evaluate the model on the test dataset
results = loaded_model.evaluate(test_data, test_labels, verbose=2)
print(f"\nTest Accuracy: {results[1]:.4f}")

# ===============================
# Example Prediction and Output
# ===============================

# Select a single test review
test_review = test_data[0]

# Make a prediction using the trained model
prediction = loaded_model.predict(np.array([test_review]))

# Display the review and prediction results
print("\n--- Sample Review ---")
print("Review:", decode_review(test_review))
print("Prediction:", prediction[0][0])
print("Actual:", test_labels[0])
