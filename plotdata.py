import matplotlib.pyplot as plt
import pandas as panda
import numpy as np


def plot_data(date=panda.Series(), consumption=panda.Series(), title_plot="",
            x_label="", y_label="", size=10, color="", ask_plot=True):
    """
    Plot function will plot the selected data
    :param date: Series of the dates of the consumption
    :param consumption: Series of the daily consumption of a year
    :param title: string the title of the plot
    :param x_label: string the label for the x-axis
    :param y_label: string the label for the y-axis
    :param size: integer determine the size of the dots in the scatter plot
    :param color: string name of the colour the dots in the  scatter plot
    :param ask_plot: boolean to determine if the plot should be shown or not
    :return: will show the plot of the daily consumption of a particular year
    """

    # create the figure for the plot
    fig, axis = plt.subplots(figsize=(15, 9))

    # create a scatter plot
    axis.scatter(x=date, y=consumption,
                marker="o", s=size, color=color)

    # give both axes labels
    axis.set(xlabel=x_label, ylabel=y_label, title=title_plot)

    # set the limits for the axes and show grid lines in plot
    plt.xlim(date.min(), date.max())
    plt.grid()

    # point on daily peak consumption in the year with a red arrow
    index = np.argmax(consumption)
    y_max = consumption[index]
    x_max = date[index]
    axis.annotate('Qdmax', xy=(x_max, y_max), arrowprops=dict(facecolor='red'))

    # show the plot if True
    if ask_plot is True:
        plt.show()
