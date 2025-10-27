# Machine Learning with Python

Analysing various machine learning algorithms and how to implement them into python scripts with data.

## Linear Regression

A basic algorithm that looks at a scatter of data points, and attempts to find the best fit line. This is typically only
suited when the data points aren't too random, as it won't be as accurate or best represented. It is best used with data
that directly correlates which each other.

## K-Nearest Neighbours (KNN)

Identifies groups of data to then categorize unknown data into groups they are nearest to / have the closest
similarities. K is a hyperparameter (configuration variable) representing the amount of closest neighbors to look for
around a data point. K in the equation should always be an odd number, as when finding it's nearest neighbors, an odd
number would be needed to break a tie.

### Finding Distance

The algorithm will "draw" a line between each of the points, to find the magnitude of each line. This can be done by
calculating the Euclidean distance using Pythagorean theorem. Having a K value too high is a potential error to run
into, as including too many neighbors could see the predicted data value being unreasonably far outside the distance of
its neighbors.

### Limitations

There are a couple of limitations with this algorithm, for one it's computationally heavy having to calculate all the
data points distances. Two it doesn't make sense to train and then save for future use, as every time it will need to
calculate distances. This only worsens with the more data and/or attributes.

## Support Vector Machine (SVM)

An SVM uses a hyperplane as a decision boundary used to separate data points into different classes. It's the optimal
separating surface found by the algorithm, aiming to maximise the distance between itself and the closest data points.
The hyperplane's dimension is one less than the number of input features. For example a line in 2D space, and a plane in
3D space.

### Hyperplane Positioning

There are infinite places to put a hyperplane when plotting data. But the ideal placement are the points furthest away
from the comparing data points also know as support vectors. In other words, the entire space between the two data
points is the margin which too
should be maximised. As it gives the best chance the data will be separated/categorized correctly, giving the highest
accuracy. Giving the best output for predicting data.

### SVM Possible Issues

Real world data doesn't usually present with a simple linear graph, worsened when more data is added. Allowing for data
points to be incorrectly categorized, and thus a very low accuracy for predicting. To help resolve this, we can use a
kernel (function) to add a dimension to a dataset. By mapping the data to a higher-dimensional space, we can separate
the points where is can be easier to use a hyperplane.