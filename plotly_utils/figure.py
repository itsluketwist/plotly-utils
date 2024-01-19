from plotly import graph_objects as go


def add_footnote(
    figure: go.Figure,
    text: str,
    x_pos: int | float = 0.5,
    y_pos: int | float = -0.1,
    color: str = "DarkSlateGrey",
    bold: bool = False,
    italic: bool = False,
    opacity: int | float = 1,
):
    """
    Add some text as a footnote, to a graph objects Figure.

    Parameters
    ----------
    figure: go.Figure
    text: str
    x_pos: int | float = 0.5
    y_pos: int | float = -0.1
    color: str = "DarkSlateGrey"
    bold: bool = False
    italic: bool = False
    opacity: int | float = 1
    """
    if bold:
        text = f"<em>{text}</em>"
    if italic:
        text = f"<i>{text}</i>"
    figure.add_annotation(
        text=text,
        xref="paper",
        yref="paper",
        x=x_pos,
        y=y_pos,
        showarrow=False,
        font_color=color,
        opacity=opacity,
    )
