import pandas as pd
import numpy as np
from PlotData import plot_data
from fun import *


def check_plausibility(data="", year=""):
    """

    :param data: Series of
    :param year:
    :return:
    """

    # plot data to show if Qdmax is in summer or not
    plot_in = input("Should the Consumption in "+year+" be shown? (Please answer in yes/no)")
    if plot_in == "yes":
        plot_data(data['Date'], data['Consumption'], "Daily Consumption", "Date [year-month]", "Consumption[M3/day]", 10,
              "navy",True)
        logging.info(f"The user input for {year} is yes.")
    elif plot_in == "no":
        plot_data(data['Date'], data['Consumption'], "Daily Consumption", "Date [year-month]", "Consumption[M3/day]",
                  10,
                  "navy", False)
        logging.info(f"The user input for {year} =! yes.")
    i = 1
    while i > 0 :
        data_verbrauch_max = data['Consumption'].max()
        date_consumption_max = data['Date'][data['Consumption'] == data_verbrauch_max]
        date_peak_day = np.array(date_consumption_max)
        month_peak_day = pd.to_datetime(date_peak_day).month
        if month_peak_day > 5 and month_peak_day < 10:
            i = 0
            data.to_excel("data\Plausible_Consumption_"+year+".xlsx", index=False)
        else:
            i = 1
            index = np.argmax(data['Consumption'])
            logging.info(f"The raw {index} was a wrong value and was extinguished.")
            data = data.drop(index)
    print("Plausibility check for the consumption in " + year +  " successfully ran.")
    logging.info(f"The plausibility check for the consumption in {year} successfully ran.")


