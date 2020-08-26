# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.5.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# + [markdown] _cell_guid="88e8ec6d-76e5-5f12-d9a6-2b40017a2b99"
# Practice of use scikit-learn classifiers on Iris dataset.
# by https://www.kaggle.com/chungyehwang/scikit-learn-classifiers-on-iris-dataset
# -

#to prevent simultaneous saving of the ipynb and the py file
# %autosave 0

# + _cell_guid="6443d6db-6440-5d93-d37c-4fde4c428ca5"
# Import data and modules
import numpy as np
from sklearn import datasets

iris = datasets.load_iris()

X = iris.data[:, [2, 3]]
y = iris.target

# + [markdown] _cell_guid="eeaf0cb8-4c35-7422-1e08-345a25ed309a"
# Next, we'll split the data into training and test datasets.
# -----------------------------------------------------------

# + _cell_guid="8393598e-1344-0e22-43fc-fdda6c75c08a"
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.35, random_state=0)

print('There are {} samples in the training set and {} samples in the test set'.format(
X_train.shape[0], X_test.shape[0]))

# + [markdown] _cell_guid="34a39b41-96cc-b560-c966-ddab1e67f65c"
# For many machine learning algorithms, it is important to scale the data. Let's do that now using sklearn.

# + _cell_guid="5867b347-4875-1e21-4313-633873a56915"
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()

sc.fit(X_train)

X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)

X_combined_std = np.vstack((X_train_std, X_test_std))
y_combined = np.hstack((y_train, y_test))

# + [markdown] _cell_guid="dc68363a-7def-d618-e190-0ddd26324bf2"
# If we plot the original data, we can see that one of the classes is linearly separable, but the other two are not.

# + _cell_guid="6f3d2990-5c6b-8ec3-4a38-63fe8ca3d241"
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt

markers = ('s', 'x', 'o')
colors = ('red', 'blue', 'lightgreen')
cmap = ListedColormap(colors[:len(np.unique(y_test))])
for idx, cl in enumerate(np.unique(y)):
    plt.scatter(x=X[y == cl, 0], y=X[y == cl, 1],
               c=cmap(idx), marker=markers[idx], label=cl)


# + _cell_guid="3c1de52a-f54f-4164-7b56-544585ff84c5"
def plot_decision_regions(X, y, classifier, test_idx=None, resolution=0.02):

    # setup marker generator and color map
    markers = ('s', 'x', 'o', '^', 'v')
    colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])

    # plot the decision surface
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
                           np.arange(x2_min, x2_max, resolution))
    Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    Z = Z.reshape(xx1.shape)
    plt.contourf(xx1, xx2, Z, alpha=0.4, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())

    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y == cl, 0], y=X[y == cl, 1],
                    alpha=0.8, c=cmap(idx),
                    marker=markers[idx], label=cl)
    
    # highlight test samples
    if test_idx:
        X_test, y_test = X[test_idx, :], y[test_idx]
        plt.scatter(X_test[:, 0], X_test[:, 1], c='', 
                   alpha=1.0, linewidth=1, marker='o',
                   s=55, label="test set")


# + [markdown] _cell_guid="09b4dc98-b068-b70c-bf35-77e82b2adc8b"
# Let's try to use a Linear SVC to predict the the labels of our test data.

# + _cell_guid="7e8e8442-ae96-b764-8ef6-67add2fa2ede"
from sklearn.svm import SVC

svm = SVC(kernel='rbf', random_state=0, gamma=.10, C=1.0)
svm.fit(X_train_std, y_train)

print('The accuracy of the svm classifier on training data is {:.2f} out of 1'.format(svm.score(X_train_std, y_train)))

print('The accuracy of the svm classifier on test data is {:.2f} out of 1'.format(svm.score(X_test_std, y_test)))

# + [markdown] _cell_guid="b76090ca-e371-6ac7-8b32-d5b404328849"
# It looks like our classifier performs pretty well. Let's visualize how the model classified the samples in our test data. 

# + _cell_guid="78cfec64-2e2a-79d4-017d-e30725060f0b"
plot_decision_regions(X=X_combined_std, y=y_combined, classifier=svm, test_idx=range(105,150))
plt.xlabel('petal length [standardized]')
plt.ylabel('petal width [standardized]')
plt.legend(loc='upper left')
plt.show()

# + [markdown] _cell_guid="090509b2-66bd-0916-571c-4224d55ffa41"
# Now, let's test out a KNN classifier.

# + _cell_guid="abd39cb6-86d8-32b6-6108-5cf69f5a4470"
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=5, p=2, metric='minkowski')
knn.fit(X_train_std, y_train)

print('The accuracy of the knn classifier is {:.2f} out of 1 on training data'.format(knn.score(X_train_std, y_train)))
print('The accuracy of the knn classifier is {:.2f} out of 1 on test data'.format(knn.score(X_test_std, y_test)))

# + _cell_guid="0e91c717-6928-e355-e15a-20b4e62ccec7"
plot_decision_regions(X=X_combined_std, y=y_combined, classifier=knn, test_idx=range(105,150))
plt.xlabel('petal length [standardized]')
plt.ylabel('petal width [standardized]')
plt.legend(loc='upper left')
plt.show()

# + [markdown] _cell_guid="05bffe84-c21b-11b1-0a02-30100d339404"
# In all classifiers, the performance on the test data was better than the training data. At least with the parameters specified in this very simple approach, the KNN algorithm seems to have performed the best. However, this may not be the case depending on the dataset and more careful parameter tuning.
