import tensorflow
import keras
import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle

data = pd.read_csv('student-mat.csv', sep=";")
data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]

predict = "G3"

X = np.array(data.drop([predict], axis=1))
y = np.array(data[predict])

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.1)

linear = linear_model.LinearRegression()
# Use x and y train data to find a best fit line, and store the line in linear
linear.fit(x_train, y_train)
# Return accuracy of the model
acc = linear.score(x_test, y_test)

# Model accuracy
print(acc)

# Coefficient numbers
print("Coefficients: ", linear.coef_)
# Y intersect
print("Intercept: ", linear.intercept_)

# Make predictions on x_test, based on the x_train training data
predictions = linear.predict(x_test)

for x in range(len(predictions)):
    # End grade prediction | input data | actual end grade
    print(round(predictions[x]), "|", x_test[x], "|", y_test[x])
