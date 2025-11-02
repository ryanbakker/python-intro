# Neural Networks

A neural network is simply a network made up of layers of neurons. Each having a state of on and off. One neuron may
determine if it's connected neurons turn or remain off or on. How the neurons and layers are connected are dependent on
the use case of the network. However, typically a fully-connected topology is used where each neuron on layer A is
connected once to each neuron on layer B. Continuing through the layers until an output is determined.

## Layer Connections

In a given network, it always begins with an input layer, and ends in an output layer. This is the main focus during
development. Each layer is connected with another by connecting certain neurons with weights and biases.

## Weights & Biases

These are adjusted while the model trains on given data, following a process of trial and error. As an example this can
be influenced by giving the model points for succeeding and take away points for failing. Depending on what the desired
outcome should be. Now depending on this reward system the network will make adjustments to each bias and weight.

## Activation Functions

Using linear functions is not a great method to use for neural networks, as it limits the network complexity. So we use
an activation or simply a nonlinear function. On a graph a linear function would give a straight line, whereas an
activation function it could be more like an S-curve for example. They can also make processing data more workable, by
transforming a neuron's output or compress the data's representation.

## Fashion-MNIST Neural Network Architecture

The process of designing the architecture of a neural network typically begins with flattening the data for the input
layer.

### Input Layer

In the chapter
three example using 28x28 images, the data will go from [[1], [2], [3]... [748]] and be changed to [1, 2, 3... 748] with
each number representing a pixel of the image. This means the initial input layer will contain 748 neurons.

### Output Layer

The output layer will consist of 10 neurons/classes representing the desired output of 0 - 9. Each of which is going to
be the network's prediction of how likely it will be the number the given neuron represents.

### Hidden Layers

Rather than having a neural network with just two layers (input and output), there will also be one hidden layer of 128
neurons. This adds complexity to the model and will allow for identifying more complex patterns in the data. Pushes the
7840 weights/balances with two layers, to 1,003,520 when using the hidden layer.

## Epochs

This is how many times the model will see the data. When the model has randomly selected the training data, it will be
shown the same selected data to the value epochs is set. We do this as changing the order of data shown to the model
will influence how it trains. Giving more variety and better accuracy when training.

## Text Classification

### Embedding Layer

In this project we use an embedding layer where for this case will be 10,000 word vectors in a dimensional space. With
each vector representing a word in the data. On creating the layer or vectors, they will have random coordinates.
Comparing two words can be understood by looking at the angle between them if hypothetically there was a linear line
from 0,0 to each of the vectors. To gain better context for words by shrinking that angle as much as possible we can
tell they're similar. Then increase the angle if they are not.

By changing the angle moving the location of each word vector we start to form sort of groups. This can be achieved by
looking at the words around the specific word vector to understand the context. As if they have similar words around it,
we can determine any similarities or differences.

### Output Layer

We get an output dimension that is known as 16 dimensions. Which is how many coefficients we have for a given vector.
Once we have the 16 dimensions, we need to scale it down a bit. As constantly using 16 dimensions would be a lot of data
for each vector.

### Network Architecture

We begin with the input that will consist of a sequence of numbers each representing a word from the data. It will be
sent to the embedding layer which will determine the word vector and assign it. This is sent to the average layer which
averages out the sizes to make it more manageable. Which is passed to the 16 neurons, where we have the dense layers.
Looking for patterns of words and classifying them into either a positive review or negative review.
Which is passed through to the output, that takes the information and presented a number between zero and one.

## Loading Data

Loading data from a set using Keras is a lot more simple to work with. However, a lot of manipulation needs to be done
when working with your own dataset. In this text classification example, characters such as "(", "?", and "!" need to be
sorted/looped through and replaced with an empty string.