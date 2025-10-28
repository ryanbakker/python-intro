# Neural Networks

A **neural network** is simply a network made up of layers of **neurons**. Each neuron produces a **numerical output**
based on the data it receives, rather than just being *on* or *off*.

Neurons pass **weighted signals** forward through connections. Each connection affects how strongly the next neuron
activates. How these neurons and layers are connected depends on the network’s **purpose or use case**.

Typically, a **fully connected** (or *dense*) topology is used — where every neuron in one layer connects to every
neuron in the next. This continues through the layers until an output is produced.

---

## Layer Connections

In any neural network, there’s always an **input layer** (where data enters) and an **output layer** (where predictions
are made). Between them can be one or more **hidden layers** that help the model learn complex patterns.

Each layer connects to the next using **weights** and **biases**, which are values the model learns and adjusts during
training.

---

## Weights & Biases

**Weights** and **biases** determine how much influence each neuron has on the next.

These values are adjusted automatically as the model trains on data, using a process called **backpropagation**. This
works by comparing the model’s predictions to the correct answers, calculating the **error (loss)**, and then adjusting
the weights and biases to reduce that error.

In simpler terms — the model learns through **trial and error**, improving its predictions each time it sees the data.

---

## Activation Functions

If we used only **linear functions**, the network would be limited in what it could learn — essentially acting like a
single straight line.

To solve this, we use **activation functions**, which introduce **nonlinearity**. These functions help the network
handle complex data and patterns.

For example:

- A **sigmoid** activation produces an *S-shaped* curve.
- A **ReLU (Rectified Linear Unit)** outputs 0 for negative inputs and the same value for positive inputs.

Activation functions also help **normalize or compress** the neuron’s output, making the network more stable and
efficient during training.

---

## Fashion-MNIST Neural Network Architecture

When designing a neural network for the **Fashion-MNIST** dataset, the process usually begins by preparing the data for
the **input layer**.

---

### Input Layer

In the example from Chapter Three using **28×28 images**, each image has **784 pixels** (28×28 = 784).  
This means we need **784 input neurons**, one for each pixel value.

> Example:  
> From `[[1], [2], [3] ... [784]]` → flattened to `[1, 2, 3 ... 784]`

---

### Hidden Layers

Rather than having only input and output layers, we add at least **one hidden layer** — for example, with **128 neurons
**.

This layer increases the model’s ability to learn complex features.

- Without a hidden layer: 784 input neurons × 10 outputs = **7,840 weights**
- With one hidden layer (128 neurons):
    - 784 × 128 = **100,352 weights** (input → hidden)
    - 128 × 10 = **1,280 weights** (hidden → output)
    - **≈ 101,632 total weights**

Adding this hidden layer makes the model far more powerful.

---

### Output Layer

The **output layer** has **10 neurons**, one for each possible class (digits **0–9**).  
Each neuron represents the model’s **confidence** that the image corresponds to that class.

For example, if the model predicts:
> [0.01, 0.03, 0.02, 0.10, 0.05, 0.70, 0.03, 0.02, 0.03, 0.01]

…it’s most confident the image represents the number **5** (since that neuron’s output is the highest).

---

## Epochs

An **epoch** refers to **one complete pass** through the entire training dataset.

During training, the data is often **shuffled** before each epoch. This helps prevent the model from memorizing the
order of the data and improves its ability to generalize to new examples.

Training for more epochs means the model will see the data multiple times, usually leading to **better accuracy** — up
to a point where improvements begin to level off.
