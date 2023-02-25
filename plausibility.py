import pandas as pd
import numpy as np
from PlotData import plot_data

# Import raw data from the Excel sheets for each year
data_2014 = pd.read_excel(r'data\Consumption_2014.xlsx')
data_2015 = pd.read_excel(r'data\Consumption_2015.xlsx')
data_2016 = pd.read_excel(r'data\Consumption_2016.xlsx')
data_2017 = pd.read_excel(r'data\Consumption_2017.xlsx')
data_2018 = pd.read_excel(r'data\Consumption_2018.xlsx')
data_2019 = pd.read_excel(r'data\Consumption_2019.xlsx')


def check_plausibility(date_series=pd.Series(), consumption_series=pd.Series(), data="", year=""):
    """

    :param date_series:
    :param consumption_series:
    :return:
    """
    # plot data to see if
    area = input("Should the Consumption in "+year+" be shown? (Please answer in yes/no)")
    if area == "yes":
        plot_data(data['Datum'], data['Verbrauch'], "Daily Consumption", "Date [year-month]", "Consumption[M3/day]", 10,
              "navy")
    i = 1
    while i > 0 :
        data_verbrauch_max = data['Verbrauch'].max()
        date_consumption_max = data['Datum'][data['Verbrauch'] == data_verbrauch_max]
        date_peak_day = np.array(date_consumption_max)
        month_peak_day = pd.to_datetime(date_peak_day).month
        if month_peak_day > 5 and month_peak_day < 10:
            i = 0
            data.to_excel("Plausible_Consumption_"+year+".xlsx", index=False)
        else:
            i = 1
            index = np.argmax(data['Verbrauch'])
            data = data.drop(index)


