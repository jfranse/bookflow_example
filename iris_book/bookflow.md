# BookFlow - MLFlow and Programmable Books

This is something I've been wanting to create for a long time. Only this year I've really started looking into it, and quite recently my enthusiasm was sparked anew by the release of Jupyter Book. So here it is, and I dub thee "BookFlow"!

BookFlow is a combination of a certain workflow and some tools. The guide that you are reading now will use MLFlow and Jupyter Book. I am also working on a version with MLFlow and R Bookdown. This Jupyter Book version is a bit of a smoother experience I think and has a lot of cool and powerful features, as long as you stick to the html output. It can also output pdf and Latex, but if those are your primary formats you should go for R Bookdown because that looks better and gives you way more control (R Bookdown also has additional formats over Jupyter Book). Otherwise all the principles are the same. 

```{margin}
**R Bookdown** has existed for quite a while now, and is very powerful. It can do all the essential things that I will do here with Jupyter Book as well. Also note that either tool can use either language, although not all Jupyter Book functionality is available for R yet. I'm using Jupyter Book because I feel the experience is just a little bit smoother, and because I was excited to do something with Jupyter Book.
```

Don't think that just because it includes the acronym "ML" in one of the tools, BookFlow is only useful for machine learning practitioners! In fact, it's useful for anyone that works with both code and data and sometimes have to communicate the results. Data scientists, academics, analysts and statisticians in any field.  

## The Point of BookFlow

The goal of BookFlow is to have both your runs and your documents in version control, connect them, and have your reports automatically update to new runs. That means:

1. Never having to manually update the numbers, tables and figures in your papers or reports after you've made a change in your code and your results changed. 
1. You are always sure that the numbers, tables and figures in your documents match with your most recent run (and are in fact from the same run!).
1. In fact we will _track_ which code and which runs created which versions of the documents. Never will you be in doubt when someone asks you "are these the most recent numbers?". And when someone shows you an old report and asks you pesky questions, you will know exactly how old it is and what's wrong with it.
1. You can always reproduce the code and the results of any old report.
1. Obviously, your documents are version controlled, so that makes editing and collaborating much easier.

These goals translate to some requirements. If you are looking at the web version of this guide, press the 'click to show' button to read about the requirements I set for these goals to get some more context and also because it may help to consider what other tools could work for this as well. Feel free to skip to the next section though.

```{toggle} Click to show my requirements
1. the source code for computations is version controlled
1. all runs performed with this code are tracked along with the inputs and the outputs in such a way that any run and result can always be reproduced. 
1. the documents about these computations and results, like papers and reports, are version controlled and written as code (like LaTeX or markdown)
1. the formatting and layout of the documents should be very customizible, so that all desireable rendered formats can be produced without the need for manual post-processing.
1. results from runs, including single numbers but also tables and figures, can be integrated into any part of a document and in any form with a minimum of effort (like in-line).
1. new or updated results can be updated in the report with a minimum of effort.

As mentioned, I will show you in the rest of this guide how MLFlow and Jupyter Book satisfy all of these requirements for the most part. We will come to the limitations and to possible future improvements later.
```

## How to Use this BookFlow Guide
All of this is actually really quite easy to set up. Just a couple pip installs and you're good to go. The next sections will show you how it works. You can copy-paste the parts your need, clone this example repository, (or, in the future, use the little package of helper functions that I'm currently working on). 

```{margin}
Please find the documentation for both [Jupyter Book](https://jupyterbook.org/intro.html) and [bookdown](https://bookdown.org/yihui/bookdown/). As I said, they are very similar, and you can use both R and Python (and more) in both of them. Note that I'm doing everything on a linux machine myself, please don't ask me about windows.
```   

Jupyter Book (and the similar R Bookdown) have many awesome features, which I encourage you to check out, but I will avoid talking about them if they are not directly and specifically relevant to BookFlow. 

This guides start with, for those that are unfamiliar with it, a super quick {ref}`primer on MLFlow <mlflow-primer>`. Then I will describe how to set up a project, and what your workflow will look like in {ref}`howto`. Following that, you will find a simple example of a document that automatically incorporates the results from runs tracked by MLFlow, this is the {ref}`main attraction <iris>` and also shows you the code for setting it up. Lastly, I will also show you an additional functionality that become available from what we've already set up: generating a {ref}`"Lab Journal" <labjournal>` automatically from your MLFlow runs.

```{warning}
Jupyter-book is pre-1.0, so its API may still change.
```

## Instant Clarification
### Does _Jupyter_ mean notebooks?

Now, the fact that it's called _Jupyter_ Book might have you worried that we will need to use notebooks and that the version control might not be all that I'm making it out to be, because notebooks are notorious for not being very suited for that kind of thing. In particular the diff's are not human-readable, which would do away with about 80% of what makes version control useful. Well, I'm happy to say that first, you don't have to work in notebooks if you don't want to, but secondly and most importantly, there is a way to use jupyter notebooks without all the aforementioned problems! It's called `jupytext`, it stores and syncs notebooks as markdown files and vice versa, and it works. I recommend having a look [here](https://jupyterbook.org/content-types/myst-notebooks.html) to learn more.



### Why do I need any of this? 

Can't I just put my normal jupyter notebooks in git and be done with it?

Well the trick here is to keep your tracking/version control of your code, your runs and your documents seperate. This way, you don't need to re-run all your code when you rebuild the document. Also, the same code can perform many runs with different settings, and you may update your code without updating your document and vice versa, so this keeps everything nice and organised.


