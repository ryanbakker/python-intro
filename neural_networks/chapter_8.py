# Text Classification Part Four - Saving & Loading Models

from tensorflow import keras

data = keras.datasets.imdb

# Load the 10,000 most frequent words in the dataset
(train_data, train_labels), (test_data, test_labels) = data.load_data(num_words=88000)

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


def review_encode(s):
    encoded = [1]

    for word in s:
        # Check if word is in dictionary
        if word.lower() in word_index:
            encoded.append(word_index[word.lower()])
        else:
            # Add <UNKNOWN> tag if word is unknown
            encoded.append(2)

    return encoded


# Use Saved Model
model = keras.models.load_model("model.keras")

with open("review_test.txt", encoding="utf-8") as f:
    for line in f.readlines():
        nline = line.replace(",", " ").replace(".", " ").replace("?", " ").replace("!", " ").replace("(", " ").replace(
            ")", " ").replace("\"", " ").strip().split(" ")
        encode = review_encode(nline)
        encode = keras.preprocessing.sequence.pad_sequences([encode], value=word_index["<PAD>"], padding="post",
                                                            maxlen=250)
        prediction = model.predict(encode)
        print(line)
        print(encode)
        print(prediction[0])
