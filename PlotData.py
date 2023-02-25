import matplotlib.pyplot as plt
import pandas as panda
import numpy as np


def plot_data(date=panda.Series(), consumption=panda.Series(), title="",
              x_label="", y_label="", size=10, color="navy"):
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

    # create figure
    fig, axes = plt.subplots(figsize=(15, 9))

    # make blue-marker scatter plot (circles with size 4)
    axes.scatter(x=date, y=consumption,
                 marker="o", s=size, color=color)

    # set axis labels
    axes.set(xlabel=x_label, ylabel=y_label, title=title)

    # show grid and set plot limits
    plt.xlim(date.min(), date.max())
    plt.grid()

    """y_max = consumption.max()
    x_max_pos = date(consumption == y_max)
    x_max = date[x_max_pos]
    axes.annotate('Qdmax', xy=(x_max, y_max), xytext=(x_max, y_max), arrowprops=dict(facecolor='black') )"""

    # show plot
    plt.show()
