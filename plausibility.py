import pandas as pd
import numpy as np
from plotdata import plot_data
from fun import *


class Plausibility:
    """
    This class is defined for the plausibility check
    """
    def __init__(self, data, year):
        """
        Define the parameters that will be used in the class.
        :param data: Data that has been read with pandas from the Excel file
        :param year: string To give the name of the file later on
        """

        self.data = data
        self.year = year

    def check_plausibility(self):
        """
        Plausibility function will check if the daily peak consumption in the data is located in summer or not.
        If not it will delete that specific consumption until new daily peak is in summer. New Excel file without the
        not plausible consumption will be created
        :return: always True
        """

        # while statement to go through the Qdmax and see if it is in Summer
        i = 1
        while i > 0:

            # get the maximum consumption
            data_cons_max = self.data['Consumption'].max()

            # get the date of the maximum consumption
            date_cons_max = self.data['Date'][self.data['Consumption'] == data_cons_max]

            # get the month of the date of the maximum consumption
            date_peak_day = np.array(date_cons_max)
            month_peak_day = pd.to_datetime(date_peak_day).month

            # if statement to see if the month is a summer month or not
            if 5 < month_peak_day < 10:
                i = 0

                # the plausible data will be exported into an Excel file
                self.data.to_excel("data\\Plausible_Consumption_" + self.year + ".xlsx", index=False)
                logging.info(f"The user input for {self.year} is yes.")
            else:
                i = 1

                # get the index where the daily consumption is maximum
                index = np.argmax(self.data['Consumption'])
                logging.info(f"The raw {index} was a wrong value and was extinguished.")

                # delete the row where the maximum daily consumption is located
                self.data = self.data.drop(index)
        print("Plausibility check for the consumption in " + self.year + " successfully ran. The Qdmax is = " +
              str(data_cons_max) + " m^3/d (" + date_cons_max.to_string(index=False) + ")")
        logging.info(f"The plausibility check for the consumption in {self.year} successfully ran.")
        return True


class PlotDaily(Plausibility):
    def plot_daily(self):
        """
        Function will plot the data of the selected year if wanted.
        :return: always True
        """

        # ask if the data should be plotted
        plot_in = input("Should the Consumption in " + self.year + " be shown? (Please answer in yes/no)")

        # if statement to let the plot be shown if wanted
        if plot_in == "yes":

            # plot data
            plot_data(self.data['Date'], self.data['Consumption'], "Daily Consumption", "Date [year-month]",
                      "Consumption[M3/day]", 10, "navy", True)
            logging.info(f"The user input for {self.year} is yes.")
        elif plot_in == "no":

            # not plotting the data
            plot_data(self.data['Date'], self.data['Consumption'], "Daily Consumption", "Date [year-month]",
                      "Consumption[M3/day]", 10, "navy", False)
            logging.info(f"The user input for {self.year} =! yes.")
        return True
