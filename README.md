# **plotly-utils**


![check code workflow](https://github.com/itsluketwist/plotly-utils/actions/workflows/check.yaml/badge.svg)


<div>
    <!-- badges from : https://shields.io/ -->
    <!-- logos available : https://simpleicons.org/ -->
    <a href="https://opensource.org/licenses/MIT">
        <img alt="MIT License" src="https://img.shields.io/badge/Licence-MIT-yellow?style=for-the-badge&logo=docs&logoColor=white" />
    </a>
    <a href="https://www.python.org/">
        <img alt="Python 3" src="https://img.shields.io/badge/Python_3-blue?style=for-the-badge&logo=python&logoColor=white" />
    </a>
    <a href="https://plotly.com/python/">
        <img alt="Plotly" src="https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=Plotly&logoColor=white" />
    </a>
</div>


## *usage*

Some simple patterns/defaults that I like to use alongside Plotly (my chosen graphing library).

Requires plotly (obviously), once installed just import into your code and use, 
mostly alongside the `graph_objects` module.

```python
from random import randint

import plotly.graph_objects as go

from plotly_utils import default_figure, write_and_display


figure = default_figure(
    title="New Example Graph",
    data=go.Scatter(
        x=list(range(10)),
        y=[randint(1, 5) for _ in range(10)],
        mode="lines+markers"
    )
)

write_and_display(
    figure=figure,
    name="example",
)

```

![Example Graph](assets/example.png)


## *installation*

Install directly from GitHub, using pip:

```shell
pip install git+https://github.com/itsluketwist/plotly-utils
```

## *development*

Clone the repository code:

```shell
git clone https://github.com/itsluketwist/plotly-utils.git
```

Once cloned, install the package locally in a virtual environment:

```shell
python -m venv venv

. venv/bin/activate

pip install -e ".[dev]"
```

Install and use pre-commit to ensure code is in a good state:

```shell
pre-commit install

pre-commit autoupdate

pre-commit run --all-files
```
