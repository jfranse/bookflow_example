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

(iris)=
# A Research Report on the Iris Dataset

+++

This is an example of a document that automatically updates when you execute new code runs. This updating happens when you build your book. 

What you see on this page by default is only the output, the way you would want a document to show up like. However, you will also see, for the purposes of this example, buttons marked 'click to show', which will show you the code that was used to enable this auto-updating from runs. 

You see that the basic code is quite straightforward. The next section on this page is the exact same thing again, but then using some helper utilities that you can find in the repo.

```{code-cell} ipython3
:tags: [hide-cell, remove-output]

%autosave 0
import mlflow
from myst_nb import glue
import pandas as pd

mlflow.set_tracking_uri('/home/jeroenf/Projects/bookflow/iris_project/mlruns')
experiment_name = 'iris'
exp_id = mlflow.get_experiment_by_name(experiment_name).experiment_id

latest_run = mlflow.get_run(mlflow.search_runs(experiment_ids=[exp_id], max_results=1).loc[0].run_id)

glue('algo', latest_run.data.params['algo'])
glue('acc', latest_run.data.metrics['acc_test'])

param_df = pd.DataFrame(latest_run.data.params.items(), columns=['Parameter','Value'])

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
im = Image.open(f'/home/jeroenf/Projects/bookflow/iris_project/mlruns/{exp_id}/{latest_run.info.run_id}/artifacts/figures/decision_region.png')
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

commit_hash = latest_run.data.tags.get('mlflow.source.git.commit', 'N/A')
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
