from typing import Any

from plotly import graph_objects as go

from .text import title_subtitle_text


DEFAULT_LAYOUT: dict[str, Any] = dict(
    template="plotly",
    width=1600,
    height=900,
    title_x=0.5,
    title_y=0.9,
    title_font_size=34,
    font_size=18,
    font_color="DarkSlateGray",
    xaxis_showgrid=False,
    margin_t=200,
)

DEFAULT_LEGEND: dict[str, Any] = dict(
    orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="center",
    x=0.5,
)


def default_figure(
    title: str,
    subtitle: str | None = None,
    x_title: str | None = None,
    y_title: str | None = None,
    data: Any = None,
) -> go.Figure:
    """
    Create a simple graph objects Figure with the default options.

    Parameters
    ----------
    title: str
    subtitle: str | None = None
    x_title: str | None = None
    y_title: str | None = None
    data: Any = None

    Returns
    -------
        go.Figure
    """
    return go.Figure(
        layout=go.Layout(
            title_text=title_subtitle_text(title=title, subtitle=subtitle),
            xaxis_title=x_title,
            yaxis_title=y_title,
            legend=DEFAULT_LEGEND,
            **DEFAULT_LAYOUT,
        ),
        data=data,
    )
