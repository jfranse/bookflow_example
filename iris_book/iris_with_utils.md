---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.12
    jupytext_version: 1.6.0
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

```{code-cell} ipython3
:tags: [remove-cell]

%load_ext autoreload
%autoreload 2
%autosave 0
```

(report_with_utils)=
# Example report with Bookflow_utils

+++

This is the same example as in the previous section, but now we are using the helper package. It's a little quicker to write if you want to do standard stuff.

```{warning}
The package bookflow_utils is a work in progress, and and proper guide to using it will also follow.
```

This is an example of a document that automatically updates when you execute new code runs. This updating happens when you build your book. 

What you see on this page by default is only the output, the way you would want a document to show up like. However, you will also see, for the purposes of this example, buttons marked 'click to show', which will show you the code that was used to enable this auto-updated from runs.

```{code-cell} ipython3
:tags: [hide-cell, remove-output]

from bookflow_utils.mlflow_to_book import BookflowConfig, BookflowHelper
config_file = '../project_config.yaml'
config = BookflowConfig(config_file) #set the experiment and also a default selection based on tags
helper = BookflowHelper(config) # this object will refer by default to the latest run of the configured experiment and tags

helper.glue_param('algo2', 'algo')
helper.glue_metric('acc2', 'acc_test')
helper.glue_all_params('params2')
```

## Methods
We have trained a {glue:text}`algo2` model on the Iris dataset. The parameters used for this model can be found in {ref}`this table<param_table2>`.

```{margin}
Code by [https://www.kaggle.com/chungyehwang/scikit-learn-classifiers-on-iris-dataset]
```

+++

```{glue:figure} params2
:name: param_table2
:figwidth: 300px

The values used for the parameters when training our {glue:text}`algo2` model.
```

+++

## Results
We achieve an accuracy of {glue:text}`acc2:.2f` on the test data. The decision boundaries can be seen in {numref}`decision_region2`.

```{code-cell} ipython3
:tags: [hide-cell]

helper.glue_image('pil_image2', 'figures/decision_region.png')
```

```{glue:figure} pil_image2
:name: decision_region2

Here we show the decision regin of our {glue:text}`algo2` model.
```

```{code-cell} ipython3
:tags: [hide-cell]

helper.glue_model_reference_metadata('int_meta_data2')
```

## Appendix
### Internal Metadata

Here we include metadata about the run whose details were included in the above document. This is useful information, for example, for cross-referencing or reproducibility when in the future you or someone else reads an old version of this document.

```{glue:figure} int_meta_data2
:name: int_meta_data2
```

```{code-cell} ipython3

```
