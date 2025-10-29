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

