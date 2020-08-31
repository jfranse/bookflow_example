---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: '0.9'
    jupytext_version: 1.5.2
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

(mlflow-primer)=
# MLFlow Primer

So after `pip install mlflow`  you can track the runs of your code like so:

```{code-cell} ipython3
:tags: [remove-output]

# prevent jupyter and your IDE from trying to make simultaneous changed
%autosave 0
import mlflow
```

```{code-cell} ipython3
:tags: [remove-cell]

import numpy as np
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier

from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt

import mlflow.sklearn

def get_data():
    iris = datasets.load_iris()

    X = iris.data[:, [2, 3]]
    y = iris.target

    return train_test_split(X, y, test_size=0.35, random_state=0)


def feature_engineering(X_train, X_test):
    sc = StandardScaler()
    sc.fit(X_train)
    X_train_std = sc.transform(X_train)
    X_test_std = sc.transform(X_test)
    return X_train_std, X_test_std

def recombine_data(X_train, X_test, y_train, y_test):
    X_combined_std = np.vstack((X_train, X_test))
    y_combined = np.hstack((y_train, y_test))
    return X_combined_std, y_combined




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

def train_knn(data, target, **params):
    knn = KNeighborsClassifier(**params)
    knn.fit(data, target)
    return knn


def train_svc(data, target, **params):
    svm = SVC(**params)
    svm.fit(data, target)
    return svm
```

```{code-cell} ipython3
:tags: [remove-output]

# set up some parameters for my code
svc_pars = dict(kernel='rbf', random_state=0, gamma=.10, C=1.0)
knn_pars = dict(n_neighbors=5, p=2, metric='minkowski')
algo = 'knn'

# set some mlflow thingamajigs
notes = "I think an knn will work better" #free text to save with a run
tags = {"test": True} # define your own tags as well
# location to save the run data
mlflow.set_tracking_uri('/home/jeroenf/Projects/bookflow/iris_project/mlruns')
# name of my experiment(= grouping of runs)
mlflow.set_experiment('iris')

run_name = f'iris_{algo}'

# let MLFlow know this is a run to track
with mlflow.start_run(run_name=run_name) as run:
    
    # -- here is just some code, it's not important for now -- 
    X_train, X_test, y_train, y_test = get_data()
    X_train, X_test = feature_engineering(X_train, X_test)

    if algo == 'svc':
        params = svc_pars
        model = train_svc(X_train, y_train, **params)
    elif algo == 'knn':
        params = knn_pars
        model = train_knn(X_train, y_train, **params)

    acc_train = model.score(X_train, y_train)
    acc_test = model.score(X_test, y_test)

    X_stack, y_stack = recombine_data(X_train, X_test, y_train, y_test)
    ## -- computations finished --
    
    # we can log parameters to this run (inputs):
    mlflow.log_params(params)
    mlflow.log_param('algo', algo)
    # and we can log metrics to this run (outputs)
    mlflow.log_metric('acc_train', acc_train)
    mlflow.log_metric('acc_test', acc_test)
    
    # and also model artifacts. 
    # even if you don't do ML, if you use sklearn, tensorflow or other common frameworks, 
    # you may still be able to save some useful objects with various log_model methods,
    # or with the log_artifact method.
    mlflow.sklearn.log_model(model, 'model')

    # we can also log plots (and basically any other file)...
    plot_decision_regions(X=X_stack, y=y_stack, classifier=model, test_idx=range(105,150))
    plt.xlabel('petal length [standardized]')
    plt.ylabel('petal width [standardized]')
    plt.legend(loc='upper left')
    plot_filename = 'decision_region.png'
    plt.savefig(plot_filename)
    # with this method
    mlflow.log_artifact(plot_filename, 'figures')

    # and also apply some tags to this run
    # the content tag is a special one
    mlflow.set_tag('mlflow.note.content', notes)
    for key, value in tags.items():
        mlflow.set_tag(key, value)
```

You don't see it here, but this run is now saved by mlflow. You can query all the runs through the python API (which we will do in the next section), but there is also an UI where you can view them conveniently.
