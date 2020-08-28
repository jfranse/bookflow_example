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

# A Research Report on the Iris Dataset

+++

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque a cursus eros. Proin efficitur lacinia dapibus. Pellentesque dui dui, sagittis viverra hendrerit ut, mollis sit amet erat. Phasellus pharetra libero vitae nibh efficitur, eget suscipit nunc gravida. Cras venenatis nisi libero, eget gravida orci placerat vitae. Aliquam pulvinar felis quis urna auctor porta. Quisque vitae nulla eu nulla commodo pharetra in vitae nibh. Curabitur vitae congue odio. Fusce vitae mollis enim. Cras mi turpis, blandit eget dignissim sed, consequat et sapien. Aenean laoreet nulla varius, gravida ligula ac, vestibulum enim.

```{code-cell} ipython3
:tags: [hide-input, remove-output]

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

params = {k:v for k, v in latest_run.data.params.items() if k != 'algo'}
param_df = pd.DataFrame(params.items(), columns=['Parameter','Value'])

glue('params', param_df, display=False)
```

## Methods
We have trained a {glue:text}`algo` model on the Iris dataset. The parameters used for this model can be found in {ref}`this table<param_table>`.

```{margin}
Code by https://www.kaggle.com/chungyehwang/scikit-learn-classifiers-on-iris-dataset
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

```{glue:figure} int_meta_data
:name: int_meta_data
```
