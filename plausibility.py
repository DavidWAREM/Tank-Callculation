import pandas as pd
import numpy as np
from plotdata import plot_data
from fun import *


class Plausibility:
    def check_plausibility(data="", year=""):
        """
        Plausibility function will check if the daily peak consumption in the data is located in summer or not.
        If not it will delete that specific consumption and find the new peak
        :param data: Data that has been read with pandas from the Excel file
        :param year: string To give the name of the file later on
        :return: always True
        """

        # plot data to show if Qdmax is in summer or not
        plot_in = input("Should the Consumption in "+year+" be shown? (Please answer in yes/no)")
        if plot_in == "yes":
            plot_data(data['Date'], data['Consumption'], "Daily Consumption", "Date [year-month]", "Consumption[M3/day]",
                    10, "navy",True)
            logging.info(f"The user input for {year} is yes.")
        elif plot_in == "no":
            plot_data(data['Date'], data['Consumption'], "Daily Consumption", "Date [year-month]", "Consumption[M3/day]",
                    10,"navy", False)
            logging.info(f"The user input for {year} =! yes.")

        # while function to go through the Qdmax and see if it is in Summer
        i = 1
        while i > 0 :
            # get the maximum consumption
            data_cons_max = data['Consumption'].max()
            # get the date of the maximum consumption
            date_cons_max = data['Date'][data['Consumption'] == data_cons_max]
            # get the month of the date of the maximum consumption
            date_peak_day = np.array(date_cons_max)
            month_peak_day = pd.to_datetime(date_peak_day).month
            if month_peak_day > 5 and month_peak_day < 10:
                i = 0
                data.to_excel("data\Plausible_Consumption_"+year+".xlsx", index=False)
                logging.info(f"The user input for {year} is yes.")
            else:
                i = 1
                index = np.argmax(data['Consumption'])
                logging.info(f"The raw {index} was a wrong value and was extinguished.")
                data = data.drop(index)
        print("Plausibility check for the consumption in " + year + " successfully ran. The Qdmax is = " +
            str(data_cons_max) + " m^3/d (" + date_cons_max.to_string(index=False) + ")")
        logging.info(f"The plausibility check for the consumption in {year} successfully ran.")
        return True



