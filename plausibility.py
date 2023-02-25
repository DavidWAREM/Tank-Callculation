import pandas as panda
import numpy as np
from PlotData import plot_data

# Import raw data from the Excel sheets for each year
data_2014 = panda.read_excel(r'data\Consumption_2014.xlsx')
data_2015 = panda.read_excel(r'data\Consumption_2015.xlsx')
data_2016 = panda.read_excel(r'data\Consumption_2016.xlsx')
data_2017 = panda.read_excel(r'data\Consumption_2017.xlsx')
data_2018 = panda.read_excel(r'data\Consumption_2018.xlsx')
data_2019 = panda.read_excel(r'data\Consumption_2019.xlsx')


def plausibility(date_series=panda.Series(), consumption_series=panda.Series(), data="", year=""):
    """

    :param date_series:
    :param consumption_series:
    :return:
    """
    # plot data to see if
    plot_data(data['Datum'], data['Verbrauch'], "Daily Consumption", "Date [year-month]", "Consumption[M3/day]", 10,
              "royalblue")
    i = 1
    while i > 0 :
        data_verbrauch_max = data['Verbrauch'].max()
        date_consumption_max = data['Datum'][data['Verbrauch'] == data_verbrauch_max]
        date_peak_day = np.array(date_consumption_max)
        month_peak_day = panda.to_datetime(date_peak_day).month
        if month_peak_day > 5 and month_peak_day < 10:
            i = 0
            data.to_excel("Plausible_Consumption_"+year+".xlsx", index=False)
            print(data_verbrauch_max)
            print(date_peak_day)
        else:
            i = 1
            index = np.argmax(data['Verbrauch'])
            data = data.drop(index)


plausibility(data_2014['Datum'], data_2014['Verbrauch'],data_2014,"2014")
plausibility(data_2015['Datum'], data_2015['Verbrauch'],data_2015,"2015")
plausibility(data_2016['Datum'], data_2016['Verbrauch'],data_2016,"2016")
plausibility(data_2017['Datum'], data_2017['Verbrauch'],data_2017,"2017")
plausibility(data_2018['Datum'], data_2018['Verbrauch'],data_2018,"2018")
plausibility(data_2019['Datum'], data_2019['Verbrauch'],data_2019,"2019")