import matplotlib.pyplot as plot
import pandas as panda

def plot_data (time_series=panda.Series(), q_series=panda.Series(), title="",
                   x_label="", y_label="", size=1, color="blue"):
    """

    :param time_series:
    :param q_series:
    :param title:
    :param size:
    :param color:
    :return:
    """

    # create figure
    fig, axes = plot.subplots(figsize=(11, 6))

    # make blue-marker scatter plot (circles with size 4)
    axes.scatter(x=time_series, y=q_series,
                 marker="o", s=size, color=color)

    # set axis labels
    axes.set(xlabel=x_label, ylabel=y_label, title=title)

    # show grid and set plot limits
    plot.xlim(time_series.min(), q_series.max())
    plot.grid()

    # show plot
    plot.show()