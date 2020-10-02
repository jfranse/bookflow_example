# BookFlow example repository

This repository is used to create <https://bookflow.jeroenfranse.com>. 

BookFlow is a set of tools and a workflow in order to track and log code runs seperately from your documents (reports, etc), but still have your documents update automatically with new runs. This should save you a lot of time manually updating your documents to new results, but also provides certain reproducibility of any old version of your documents and results. Please follow the link to the guide above to learn more about it.

## What  you need to know about this repo
If you are looking at this repository, you are either interested in the exact code I used in this example, or you want to use it to set up your own BookFlow.

### The code
The directory `iris_book` contains the actual project code. It is a very straightforward example (adapted from [this kaggle kernel](https://www.kaggle.com/chungyehwang/scikit-learn-classifiers-on-iris-dataset)).

Run the python script that is in this directory from the root of this repository, and the mlflow runs will be stored in `iris_project/mlruns`. 

Adapt the parameters, and mlflow tags and notes for the run at the top of the `"__main__"` function.  

### The document
The directory `iris_book` contains all the content and configs of the document. Some of the `.md` files are actually MyST notebooks and can be opened with Jupyter Notebook if you have jupytext installed. Saving them from Jupyter Notebook will create are corresponding synced `.ipynb` file. 

The `iris_with_utils` notebook requires the bookflow utilities package, which can be found [here](https://github.com/jfranse/bookflow_utils). 

To build the book run `jupyter-book build iris_book/` from the repository root, or use the shortcut `make book` as defined in the Makefile. The produced book can be found in the directory `_build/html`.  
