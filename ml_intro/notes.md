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

## Unsupervised Machine Learning Algorithms

Algorithms that analyse and model datasets without labeled data. This is to discover hidden patterns, structures, or
relationships within the dataset independently. This is ideal for datasets with a lack of labels, or for discovery of
unknown patterns and relationships.

### K-Means Clustering Algorithm

The K represents how many clusters in an output. With a various amount of clusters, it is important to correctly
implement centroids that will be used as a sort of index that can be referenced for assigning each data point to the
correct cluster. The centroids a first given random positions in the dataset, with an evenly distributed divide being
determined between. The data points are then assigned their cluster based on this division. The centroid is then
repositioned to be in the average location of it's clusters data points.

The steps are then followed again by evenly
dividing the clusters based on the new positions of the centroids. Reassigning the datapoints based on their position in
relation to the division. This is followed by once again repositioning the centroids, dividing, and reassigning. Being
repeated until after each revision data points are no longer needed to be reassigned to a different cluster.

### K-Means Clustering Limiations

The algorithm can become extremely computationally heavy very quickly. This is because depending on centroid, feature,
and data point amounts. As each amount increases the calculations needed to determine which cluster should be assigned
for each datapoint is compounded.