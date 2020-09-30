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

```{code-cell} ipython3
:tags: [remove-cell]

from bookflow_utils.mlflow_to_book import BookflowConfig, BookflowHelper
from bookflow_utils.mlflow_to_book import glue_image_by_uri
from myst_nb import glue

config_file = '../project_config.yaml'

config = BookflowConfig(config_file)

#set_tracking_uri(config)

helper = BookflowHelper(config)

glue('lab_exp_name', helper.experiment_name)
```

(labjournal)=
# Lab Journal - Experiment: {glue:}`lab_exp_name`

This is another possibility that presents itself by using BookFlow: a lab journal. Here, we automatically generate a journal of the logged runs, by date and time with the pertinent information. This view is, in my opinion, more useful (quicker) for getting a good sense of what you've been doing lately and why, than the default MLFlow UI. 

We show the date and run name as the main header, followed by the note. Obviously this requires that you actually put in some useful information in the note. To make a lab journal useful, it would be along the lines of "I changed this and that in the code, and this parameter, which I did for these reasons and now I'm expecting the following to happen". We also show the main parameters and the main metrics.

Further we then provide a fold-out section for the full parameters and metrics, and figures and tables. This puts a lot of information at first glance, and much more information at a single mouse-click, without cluttering the view, or having to go back-and-forth between MLFlow pages.

The code to create a single entry here isn't really different from any of the other things we already did. However, you would never write the entries one-by-one yourself, obviously. The point would be to write a script to generate it for you, based on your MLFlow tracker. This is a work in progress effort. It is a bit hacky and I guess it would be better to just extend the MLFlow UI, but I don't know how to do that. I invite you to beat me to it! :)

```{code-cell} ipython3
:tags: [remove-cell]

latest_run = helper.get_latest_run()
```

```{code-cell} ipython3
:tags: [remove-cell]

latest_run
```

```{code-cell} ipython3
:tags: [remove-cell]

latest_run.data.params
```

```{code-cell} ipython3
:tags: [remove-cell]

import pandas as pd
import time
def journal_entry(run, entry_num):
    header = dict(
        datetime = time.strftime('%Y-%m-%d %H:%M', time.localtime(run.info.end_time / 1000.)),
        run_name = run.data.tags['mlflow.runName'],
        description = run.data.tags['mlflow.note.content'],
        )
    parameters_table = (pd.DataFrame(run.data.params.items(), columns=['Parameter','Value']).
                        set_index('Parameter', drop=True).transpose())
    return header, parameters_table
```

```{code-cell} ipython3
:tags: [remove-cell]

entry_num = 1

header, params = journal_entry(latest_run, entry_num)

glue(f'dt_{entry_num}', header['datetime'])
glue(f'name_{entry_num}', header['run_name'])
glue(f'description_{entry_num}', header['description'])

glue(f'lab_params_{entry_num}', params.transpose())
```

```{code-cell} ipython3
:tags: [remove-cell]

from PIL import Image
im_uri = f'/home/jeroenf/Projects/bookflow/iris_project/mlruns/{helper.experiment_id}/{latest_run.info.run_id}/artifacts/figures/decision_region.png'
im = Image.open(im_uri)
glue(f'lab_image_{entry_num}', im, display=False)
```

### {glue:text}`dt_1` -- {glue:}`name_1`
> {glue:text}`description_1`

+++

`````{margin}
````{admonition} Parameters
:class: dropdown
```{glue:figure} lab_params_1
```
````
`````

```{code-cell} ipython3
:tags: [remove-input, hide-output, remove-cell]

# I can insert it right here as output of a code cell if I want
params
```

```{code-cell} ipython3
:tags: [remove-cell]

# or I can glue the figure within a toggle
```

````{admonition} Figures
:class: dropdown
```{glue:figure} lab_image_1
:name: decision region
Decision regions.
```
````
