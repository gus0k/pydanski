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

