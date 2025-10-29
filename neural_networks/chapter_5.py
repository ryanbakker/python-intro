# Text Classification Part One
from tensorflow import keras

data = keras.datasets.imdb

# Load the 10,000 most frequent words in the dataset
(train_data, train_labels, test_data, test_labels) = data.load_data(num_words=10000)

word_index = data.get_word_index()

# Assign words to encoded integers
word_inex = {k: (v + 3) for k, v in word_index.items()}

word_index["<PAD>"] = 0
word_index["<START>"] = 1
word_index["<UNK>"] = 2
word_index["<UNUSED>"] = 3

# Reverse index so integer points to word, rather than word points to integer
reverse_word_index = dict([(value, key) for (key, value) in word_index.items()])

# Make each movie review the same length
train_data = keras.preprocessing.sequence.pad_sequences(train_data, value=word_index["<PAD>"], padding="post",
                                                        maxlen=250)
test_data = keras.preprocessing.sequence.pad_sequences(test_data, value=word_index["<PAD>"], padding="post", maxlen=250)


# Decode the training and testing data into readable words
def decode_review(text):
    return " ".join([reverse_word_index.get(i, "?") for i in text])


# Define model architecture
model = keras.Sequential()
model.add(keras.layers.Embedding(10000, 16))
model.add(keras.layers.GlobalAveragePooling1D())
model.add(keras.layers.Dense(16, activation="relu"))
model.add(keras.layers.Dense(1, activation="sigmoid"))
