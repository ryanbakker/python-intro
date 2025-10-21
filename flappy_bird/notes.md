### Project Overview

This project shows an AI training itself on how to play the game "Flappy Bird". It starts of completely random, with not
having any knowledge on what to do or how the game operates. After many generations it picks up on patterns, figuring
out how to progress further into the game using the genetic algorithm NEAT (Neuro Evolution of Augmenting Topologies).

### AI Game Progression Analysis

Text here... how many generations does it take...

### NEAT Algorithm Implementation

The algorithm uses neural networks consisting of layers, input and output. With the input including the position of the
bird, and the distance to the top and bottom pipes. In this case only the Y position of the bird needs to be given, as
it does not move along the X axis in the program. The output layer is going to tell the AI what to do, in this case
whether to jump or not jump. Individual connections between each input and the output have weights to determine how
strong that connection is. Changing the quality of the AI.

Using the TanH activation function, the AI has the set rule so if the output is greater than 0.5 it is to jump, else not
to jump. NEAT is used to find the weights of the different connections through a population of 10 "Flappy Birds" and
continuously retrying over multiple generations. Starting off with random bias' and weights, they will get more accurate
as the fitness of the birds improves through various generations.

The birds with the highest fitness score from the most recent population are then used to "mutate and breed" into the
next population. Giving the new birds the best possible chance to proceed further in the game. It will begin with a very
basic neural network, progressively getting more complex by adding nodes, connections, and neurons etc. However, the
algorithm will use a more simple network if it achieves higher than a more complex one. This is more favourable in the
implementation.