import sklearn
from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing
import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv('car.data')

# Encode string data into integers
le = preprocessing.LabelEncoder()
buying = le.fit_transform(list(data['buying']))
maint = le.fit_transform(list(data['maint']))
door = le.fit_transform(list(data['door']))
persons = le.fit_transform(list(data['persons']))
lug_boot = le.fit_transform(list(data['lug_boot']))
safety = le.fit_transform(list(data['safety']))
cls = le.fit_transform(list(data['class']))

predict = "class"

X = list(zip(buying, maint, door, persons, lug_boot, safety))
y = list(cls)

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.1)

model = KNeighborsClassifier(n_neighbors=9)
model.fit(x_train, y_train)
acc = model.score(x_test, y_test)
print("Accuracy:", acc)

# 3D Visualization of feature relationships
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Safety (Z), Maintenance (Y), and Class (Color)
x_vals = maint
y_vals = safety
z_vals = cls

scatter = ax.scatter(x_vals, y_vals, z_vals, c=cls, cmap='viridis', s=50)

ax.set_xlabel('Maintenance')
ax.set_ylabel('Safety')
ax.set_zlabel('Class')
ax.set_title('3D Feature Relationship: Maintenance vs Safety vs Class')

# Add legend (custom color mapping)
legend_labels = ["unacc", "acc", "good", "vgood"]
legend = ax.legend(handles=scatter.legend_elements()[0], labels=legend_labels, title="Class")
ax.add_artist(legend)

plt.show()
