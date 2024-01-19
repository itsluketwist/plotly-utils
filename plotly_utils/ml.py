from typing import Sequence

from plotly import graph_objects as go
from plotly.subplots import make_subplots

from .default import DEFAULT_LAYOUT, DEFAULT_LEGEND
from .figure import add_footnote
from .text import standout, title_subtitle_text


def create_learning_curves(
    train_acc: Sequence,
    train_loss: Sequence,
    test_acc: Sequence,
    test_loss: Sequence,
    epochs: int | None = None,
    title: str = "Learning Curves",
    project: str | None = None,
    subtitle: str | None = None,
    footnote_text: str | None = None,
    colors: list[str] | None = None,
):
    curves = ["training", "testing"]

    if colors is None:
        colors = ["DodgerBlue", "Coral"]

    if project is not None:
        title = f"{standout(project, 'DarkSlateBlue')} {title}"

    if epochs is None:
        epochs = len(train_acc)
    x_data = [str(n + 1) for n in range(epochs)]

    figure = make_subplots(rows=1, cols=2, shared_xaxes=True)
    figure.update_layout(
        title_text=title_subtitle_text(title=title, subtitle=subtitle),
        legend=DEFAULT_LEGEND,
        **DEFAULT_LAYOUT,
    )
    figure.update_yaxes(title_text="Accuracy Percentage", row=1, col=1)
    figure.update_yaxes(title_text="Loss Value", row=1, col=2)
    figure.update_xaxes(title_text=standout("εpochs", "DarkSlateBlue"))

    if footnote_text:
        add_footnote(
            figure=figure,
            text=footnote_text,
        )

    for i, y_data in enumerate([train_acc, test_acc]):
        figure.add_trace(
            go.Scatter(
                name=curves[i],
                x=x_data,
                y=y_data,
                marker_color=colors[i],
                mode="lines",
                line_width=3,
                showlegend=True,
            ),
            row=1,
            col=1,
        )

    for i, y_data in enumerate([train_loss, test_loss]):
        figure.add_trace(
            go.Scatter(
                name=curves[i],
                x=x_data,
                y=y_data,
                marker_color=colors[i],
                mode="lines",
                line_width=3,
                showlegend=False,
            ),
            row=1,
            col=2,
        )

    return figure
