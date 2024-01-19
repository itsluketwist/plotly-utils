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
    if colors is None:
        colors = ["DodgerBlue", "Coral"]

    if project is not None:
        title = f"{standout(project, colors[0])} {title}"

    if epochs is None:
        epochs = len(train_acc)
    x_data = [str(n + 1) for n in range(epochs)]

    figure = make_subplots(rows=1, cols=2)
    figure.update_layout(
        title_text=title_subtitle_text(title=title, subtitle=subtitle),
        legend=DEFAULT_LEGEND,
        **DEFAULT_LAYOUT,
    )
    figure.update_yaxes(title_text="Accuracy Percentage", row=1, col=1)
    figure.update_yaxes(title_text="Loss Value", row=1, col=2)

    if footnote_text:
        add_footnote(
            figure=figure,
            text=footnote_text,
        )

    acc_data = [
        ("training", train_acc),
        ("validation", test_acc),
    ]
    for i, y_data in enumerate(acc_data):
        figure.add_trace(
            go.Scatter(
                name=y_data[0],
                x=x_data,
                y=y_data[1],
                marker_color=colors[i],
                mode="lines",
                line_width=3,
                showlegend=True,
            ),
            row=1,
            col=1,
        )

    loss_data = [
        ("training", train_loss),
        ("validation", test_loss),
    ]
    for i, y_data in enumerate(loss_data):
        figure.add_trace(
            go.Scatter(
                name=y_data[0],
                x=x_data,
                y=y_data[1],
                marker_color=colors[i],
                mode="lines",
                line_width=3,
                showlegend=False,
            ),
            row=1,
            col=2,
        )

    return figure
