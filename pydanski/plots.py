import matplotlib.pyplot as plt


def remove_duplicate_legends(fig, ax):
    """
    Removes duplicates legends from the provided axis

    fig: matplotlib figure object
    ax: matplotlib axis object
    """
    handles, labels = fig.gca().get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    ax.legend(by_label.values(), by_label.keys())
    return None

def add_text_to_bars(fig, ax, texts):
    """
    Adds custom text on top of a vertical barplot
    image.
    It also adjusts the y-axis to make sure that
    the new labels fit.

    Args:
        fig: matplotlib figure object
        ax: matplotlib axis object
        texts: list of str
            Texts to add on top of each bar.

    """

    for j, p in enumerate(ax.patches):
        x_ = p.xy[0] + p.get_width() / 2
        y_ = (p.xy[1] + p.get_height()) * 1.1
        ax.text(x_, y_, texts[j], ha="center")

    ax.set_ylim(ax.get_ylim()[0], ax.get_ylim()[1] * 1.2)
    return None
