(howto)=
# BookFlow Guide

## Installation
`pip install -U mlflow jupyter-book jupytext` 

## Initial set-up
1. Get or write your actual code, the stuff that's going to do you computations and create your results. Put it in a git repo. It's fine if you have a seperate repo for your code, but it's also fine if you want the code and the book in the same repo.
1. Insert the mlflow commands in your code if you had not already done that. Recall this is the stuff that makes each run be logged and saved. 
1. Initialize your jupyter-book, for example using the built-in template:
`jupyter-book create mybookname`. This will create a directory called 'mybookname'. Make this a git repo, or make this book directory part of your project repo.
1. Follow the Jupyter Book docs for information about various config options you have. 

## Creating book content
Jupyter-book can contain [different file types](https://jupyterbook.org/content-types/index.html). I recommend regular markdown files if there is no code involved, and MyST markdown if there is. 

Creating a new MyST page for your book:
1. Create a new normal jupyter notebook, save it with the filename you want. 
1. In your notebook interface, go to File > Jupytext > Pair notebook with MyST markdown. This will create a markdown file in the same folder with the same name as the notebook (apart from the extension).
1. You can now also open the .md file in your favorite IDE if you want to.  
1. Add `%autosave 0` to the top of your notebook, to prevent your IDE and jupyter notebook from trying to save to the same file simultaneously.
1. From now on, whenever you save your jupyter notebook (.ipynb), jupytext will sync it with the MyST file (.md), and vice versa. 
1. Add _only_ the MyST file (.md) to your git. Because of the syncing, if you pull a change to your MyST file, the jupyter-notebook will be automatically updated as well.

## The BookFlow
This is what your day-to-day work with BookFlow with look like

1. Run your code. This results in a run being logged to MLFlow. 
1. Build your book `jupyter-book build mybookname`

That's it. Now your "book" (or paper, or report) is updated with all the results from the latest run. Keep repeating. When you want to change something about your book, perform the build command again. 

```{tip}
Remember to keep code runners seperate from your book. Firstly, this way you don't have to re-run your code when you change something about your book. Secondly, MLFlow will log the git commit hash of the code to the run, so it's cleaner if you seperate commits to the code runners and commits to the book.
```

## Tips and Tricks

- static page versus pdf versus latex

### PDF and LaTeX
The default output format of Jupyter Book is the html page you are probably look at now. For PDF and Latex, see <https://jupyterbook.org/advanced/pdf.html>, but here's the essentials:

- pdf: to setup once on your system run `pip install pyppeteer & pyppeteer-install`, then `jupyter-book build mybook/ --builder htmlpdf` 

 
