# BookFlow - Jupyter-book and MLFlow - A match made in heaven

This is what I've been looking for, for the past eight years. I dub thee "BookFlow"! A combination of the recently released Jupyter-book and MLFlow. Don't be fooled though, this is not just useful for machine learning practitioners, but for anyone that works with both code and data. Data scientists, academics, analysts and statisticians in any field. 

```{margin}
Also something to get out of the way asap, is that everything I'm going to show you can also be done with *R bookdown* instead! Yes, that has existed for much longer already and has all the same essential features. Yet somehow jupyter-book just seems a little bit of a smoother experience to me after a little playing around with both, and it just made me that bit more ethusiastic and here we are. 

Actually, this type of 'side-note' or 'margin' is not available in all bookdown styles, maybe that's why I like jupyter-book better. 
```

The goal of BookFlow is to have both your runs and your documents in version control, connect them, and have your reports automatically update to new runs. That means:

1. Never having to manually update the numbers, tables and figures in your papers or reports after you've made a change in your code and your results changed. 
1. You are always sure that the numbers, tables and figures in your documents match with your most recent run.
1. In fact we will _track_ which code and runs created which versions of the documents. Never will you be in doubt when someone asks you "are these the most recent numbers?". And when someone shows you an old report and asks you pesky questions, you will know exactly how old it is and what's wrong with it.
1. If needed you can always reproduce the code and the results of any old report.
1. Obviously, your documents are version controlled, so that makes editing and collaborating much easier.

Now, the fact that it's called _jupyter_-book might have you worried that we will need to use notebooks and that the version control might not be all that I'm making it out to be, because notebooks are notorious for not being very suited for that kind of thing. In particular the diff's are not human-readable, which would do away with about 80% of what makes version control useful. Well, I'm happy to say that first, you don't have to work in notebooks if you don't want to, but secondly and most importantly, there is a way to use jupyter notebooks without all the aforementioned problems! It's called `jupytext`, it stores and syncs notebooks as markdown files and vice versa, and it works. I recommend having a look [here](https://jupyterbook.org/content-types/myst-notebooks.html) to learn more.

All of this is actually really quite easy to set up. Just a couple pip installs and you're good to go. The following sections will show you how it works. You can copy-paste the parts your need, clone this example repository, (or, in the future, use the little package of helper functions that I'm currently working on). 

```{margin}
Please fin the documentation for both [jupyter-book](https://jupyterbook.org/intro.html) and [bookdown](https://bookdown.org/yihui/bookdown/). As I said, they are very similar, and you can use both R and Python (and more) in both of them. Note that I'm doing everything on a linux machine.
```   

Jupyter-book (and R bookdown) have many awesome features, which I encourage you to check out, but I will avoid talking about them if they are not directly and specifically relevant to BookFlow. 

## Why do you need all of this? 

Can't I just put my normal jupyter notebooks in git and be done with it?

Well the trick here is to keep your tracking/version control of your code, your runs and your documents seperate. This way, you don't need to re-run all your code when you rebuild the document. Also, the same code can perform many runs with different settings, and you may update your code without updating your document and vice versa, so this keeps everything nice and organised.

## How to use the following "book"

To begin with, for those that are unfamiliar with it, a super quick {ref}`primer on MLFlow <mlflow-primer>`. Then I will describe how to set up a project, and what your workflow will look like in {ref}`howto`. Following that, you will find a simple example of a document that automatically incorporates the results from runs tracked by MLFlow, this is the {ref}`main attraction <iris>`. Lastly, I will also show you an additional functionality that become available from what we've already set up: generating a {ref}`"Lab Journal" <labjournal>` automatically from your MLFlow runs.

```{warning}
Jupyter-book is pre-1.0, so its API may still change.
```