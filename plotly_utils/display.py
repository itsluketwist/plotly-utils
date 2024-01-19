from IPython.display import Image, display
from plotly import graph_objects as go


def write_and_display(
    figure: go.Figure | list[go.Figure],
    name: str,
    path: str = "./images/",
    show: bool = False,
):
    """
    Save a Figure to file, and display it (if in a notebook).

    Parameters
    ----------
    figure: go.Figure | list[go.Figure]
    name: str
    path: str = "./images/"
    show: bool = False
    """
    if isinstance(figure, list):
        for idx, fig in enumerate(figure):
            write_and_display(
                figure=fig,
                name=f"{name}_{idx + 1}",
                path=path,
                show=show,
            )
    else:
        full_path = f"{path}{name}.png"
        figure.write_image(full_path)
        if show:
            display(Image(filename=full_path))
