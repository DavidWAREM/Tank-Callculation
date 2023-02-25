import matplotlib.pyplot as plt
import pandas as panda
import numpy as np


def plot_data(date=panda.Series(), consumption=panda.Series(), title="",
              x_label="", y_label="", size=10, color=""):
    """

    :param date:
    :param consumption:
    :param title:
    :param x_label:
    :param y_label:
    :param size:
    :param color:
    :return:
    """

    # create the figure for the plot
    fig, axis = plt.subplots(figsize=(15, 9))

    # create a scatter plot
    axis.scatter(x=date, y=consumption,
                 marker="o", s=size, color=color)

    # give both axes labels
    axis.set(xlabel=x_label, ylabel=y_label, title=title)

    # set the limits for the axes and show grid lines in plot
    plt.xlim(date.min(), date.max())
    plt.grid()

    # point on Qdmax in the year with a red arrow
    index = np.argmax(consumption)
    y_max = consumption[index]
    x_max = date[index]
    axis.annotate('Qdmax', xy=(x_max, y_max), arrowprops=dict(facecolor='red'))

    # show the plot
    plt.show()
