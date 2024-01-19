def title_subtitle_text(
    title: str,
    subtitle: str | None = None,
    bold_subtitle: bool = False,
) -> str:
    """
    Create a title string, including a smaller subtitle.

    Parameters
    ----------
    title: str
    subtitle: str | None = None
    bold_subtitle: bool = False

    Returns
    -------
    str
    """
    if subtitle is not None:
        if bold_subtitle:
            subtitle = f"<em>{subtitle}</em>"
        return f"{title}<br><br><sup>{subtitle}</sup>"
    else:
        return title


def readable_large_number(
    number: int | float,
    bold: bool = True,
) -> str:
    """
    Convert a large number to a more human-understandable string version.

    Parameters
    ----------
    number: int | float
    bold: bool = True

    Returns
    -------
    str
        The given large number as a more readable string.
    """
    number = int(number)

    # under 10 thousand
    if number < 10e4:
        num_str = f"{number}"

    # under 1 million
    elif number < 10e6:
        # display thousands
        num_str = f"{round(number/1000):,}k"

    # under 1 billion
    elif number < 10e9:
        # display millions
        num_str = f"{round(number/10e6):,}m"

    # over 1 billion
    else:
        # display billions
        num_str = f"{round(number / 10e9):,}b"

    return f"<b>{num_str}</b>" if bold else num_str


def standout(
    text: str,
    color: str,
) -> str:
    """
    Use html styling to apply colour and weighting to text, to make it stand out.

    Parameters
    ----------
    text: str
    color: str

    Returns
    -------
    str
        The HTML tag string containing the styled text.
    """
    return f"<span style='color: {color}; font-weight:bold'>{text}</span>"
