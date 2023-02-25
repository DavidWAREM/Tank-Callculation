import pandas as pd
from plausibility import check_plausibility
from fun import *
from Category import Tank

# Import raw data from the Excel sheets for each year
data_2014 = pd.read_excel(r'data\\Consumption_2014.xlsx')
data_2015 = pd.read_excel(r'data\\Consumption_2015.xlsx')
data_2016 = pd.read_excel(r'data\\Consumption_2016.xlsx')
data_2017 = pd.read_excel(r'data\\Consumption_2017.xlsx')
data_2018 = pd.read_excel(r'data\\Consumption_2018.xlsx')
data_2019 = pd.read_excel(r'data\\Consumption_2019.xlsx')

print("The algorythm will calculate, if the given tank is big enough for the given outflow data,"
      "\nregarding the German law for water supply facilities.")

if __name__ == '__main__':
    start_logging()
    check_plausibility(data_2014['Datum'], data_2014['Verbrauch'], data_2014, "2014")
    check_plausibility(data_2015['Datum'], data_2015['Verbrauch'], data_2015, "2015")
    check_plausibility(data_2016['Datum'], data_2016['Verbrauch'], data_2016, "2016")
    check_plausibility(data_2017['Datum'], data_2017['Verbrauch'], data_2017, "2017")
    check_plausibility(data_2018['Datum'], data_2018['Verbrauch'], data_2018, "2018")
    check_plausibility(data_2019['Datum'], data_2019['Verbrauch'], data_2019, "2019")
    my_tank = Tank()
    my_tank.tank_data()
    my_tank.category_1()
    my_tank.category_2()
    my_tank.category_3()
    my_tank.final_calculation()
