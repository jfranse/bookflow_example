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
:tags: [remove-cell]

%autosave 0

import mlflow
from myst_nb import glue
import pandas as pd

mlflow.set_tracking_uri('/home/jeroenf/Projects/jupyterflow/iris_project/mlruns')

latest_run = mlflow.get_run(mlflow.search_runs(max_results=1).loc[0].run_id)
```

```{code-cell} ipython3
:tags: [remove-cell]

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
:tags: [remove-cell]

# how to 
from PIL import Image
im = Image.open(f'/home/jeroenf/Projects/jupyterflow/iris_project/mlruns/0/{latest_run.info.run_id}/artifacts/figures/decision_region.png')
glue('pil_image', im, display=False)
```

```{glue:figure} pil_image
:name: decision_region

Here we show the decision regin of our {glue:text}`algo` model.
```

```{code-cell} ipython3
latest_run
```

```{code-cell} ipython3
latest_run.data.
```

## Appendix
### Internal Metadata
