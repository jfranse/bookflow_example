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

```{code-cell} ipython3
:tags: [remove-cell]

%load_ext autoreload
%autoreload 2
%autosave 0
```

(iris)=
# A Research Report on the Iris Dataset

+++

This is an example of a document that automatically updates when you execute new code runs. This updating happens when you build your book. 

What you see on this page by default is only the autoput, the way you would want a document to show up like. However, you will also see, for the purposes of this example, buttons marked 'click to show', which will show you the code that was used to enable this auto-updated from runs. 

```{code-cell} ipython3
:tags: [remove-cell]

from myst_nb import glue
from bookflow_utils.mlflow_to_book import BookflowConfig, BookflowHelper
config_file = '../project_config.yaml'
config = BookflowConfig(config_file)
helper = BookflowHelper(config)

latest_run = helper.get_latest_run()

glue('algo', latest_run.data.params['algo'])
glue('acc', latest_run.data.metrics['acc_test'])
param_df = helper.get_params_as_df(latest_run)
glue('params', param_df, display=False)
```

## Methods
We have trained a {glue:text}`algo` model on the Iris dataset. The parameters used for this model can be found in {ref}`this table<param_table>`.

```{margin}
Code by [https://www.kaggle.com/chungyehwang/scikit-learn-classifiers-on-iris-dataset]
```

+++

```{glue:figure} params
:name: param_table
:figwidth: 300px

The values used for the parameters when training our {glue:text}`algo` model.
```

+++

## Results
We achieve an accuracy of {glue:text}`acc:.2f` on the test data. The decision boundaries can be seen in {numref}`decision_region`.

```{code-cell} ipython3
:tags: [hide-cell]

from PIL import Image
im = Image.open(f'/home/jeroenf/Projects/bookflow/iris_project/mlruns/{helper.experiment_id}/{latest_run.info.run_id}/artifacts/figures/decision_region.png')
glue('pil_image', im, display=False)
```

```{glue:figure} pil_image
:name: decision_region

Here we show the decision regin of our {glue:text}`algo` model.
```

```{code-cell} ipython3
:tags: [remove-cell]

latest_run
```

```{code-cell} ipython3
:tags: [hide-cell, remove-output]

import time

try:
    commit_hash = latest_run.data.tags['mlflow.source.git.commit']
except:
    commit_hash = 'N/A'
run_id = latest_run.info.run_id
run_end_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(latest_run.info.end_time/1000.))
internal_meta_data = dict(
    commit_hash=commit_hash,
    run_id = run_id,
    run_end_time = run_end_time
)

glue('int_meta_data', internal_meta_data)
```

## Appendix
### Internal Metadata

Here we include metadata about the run whose details were included in the above document. This is useful information for cross-referencing when in the future you or someone else reads, for example, an old version of this document.

```{glue:figure} int_meta_data
:name: int_meta_data
```
