import pandas as pd
import numpy as np
from plotdata import plot_data
from fun import *


class Plausibility:
    """Author: Graciella Bawole"""

    def __init__(self, year):
        self.year = year
        self.loop = 1

    def check_plausibility(self, data):
        """
        Plausibility function will check if the daily peak consumption in the data is located in summer or not.
        If not it will delete that specific consumption and find the new peak
        :param data: Data that has been read with pandas from the Excel file
        :param year: string To give the name of the file later on
        :return: always True
        """
        #self.data = pd.read_excel(r'data\\Consumption_2014.xlsx')
        # plot data to show if Qdmax is in summer or not
        """plot_in = input("Should the Consumption in "+ self.year +" be shown? (Please answer in yes/no)")
        if plot_in == "yes":
            plot_data(self.data['Date'], self.data['Consumption'], "Daily Consumption", "Date [year-month]", "Consumption[M3/day]",
                    10, "navy",True)
            logging.info(f"The user input for {self.year} is yes.")
        elif plot_in == "no":
            plot_data(self.data['Date'], self.data['Consumption'], "Daily Consumption", "Date [year-month]", "Consumption[M3/day]",
                    10,"navy", False)
            logging.info(f"The user input for {self.year} =! yes.")"""

        # while function to go through the Qdmax and see if it is in Summer
        while self.loop > 0 :
            # get the maximum consumption
            data_cons_max = data['Consumption'].max()
            # get the date of the maximum consumption
            date_cons_max = data['Date'][data['Consumption'] == data_cons_max]
            # get the month of the date of the maximum consumption
            date_peak_day = np.array(date_cons_max)
            month_peak_day = pd.to_datetime(date_peak_day).month
            if month_peak_day > 5 and month_peak_day < 10:
                self.loop = 0
                data.to_excel("data\Plausible_Consumption_"+self.year+".xlsx", index=False)
                logging.info(f"The user input for {self.year} is yes.")
            else:
                self.loop = 1
                index = np.argmax(data['Consumption'])
                logging.info(f"The raw {index} was a wrong value and was extinguished.")
                data = data.drop(index)
        print("Plausibility check for the consumption in " + self.year + " successfully ran. The Qdmax is = " +
            str(data_cons_max) + " m^3/d (" + date_cons_max.to_string(index=False) + ")")
        logging.info(f"The plausibility check for the consumption in {self.year} successfully ran.")
        return True

class PlotDaily(Plausibility):
    """Author: Ashwini Rajashekhar Mudigoudar"""
    def plot_daily(self,data):
        plot_data(data['Date'], data['Consumption'], "Daily Consumption", "Date [year-month]",
                  "Consumption[M3/day]",
                  10, "navy", True)
        plot_in = input("Should the Consumption in "+ self.year +" be shown? (Please answer in yes/no)")
        if plot_in == "yes":
            plot_data(data['Date'], data['Consumption'], "Daily Consumption", "Date [year-month]", "Consumption[M3/day]",
                    10, "navy",True)
            logging.info(f"The user input for {self.year} is yes.")
        elif plot_in == "no":
            plot_data(data['Date'], data['Consumption'], "Daily Consumption", "Date [year-month]", "Consumption[M3/day]",
                    10,"navy", False)
            logging.info(f"The user input for {self.year} =! yes.")


