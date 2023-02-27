import pandas as pd
from plausibility import *
from fun import *
from category import Tank

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
    p_2014 = Plausibility("2014")
    p_2014.check_plausibility(data_2014)
    pl_2014 = PlotDaily("2014")
    pl_2014.plot_daily(data_2014)
    my_tank = Tank()
    my_tank.tank_data()
    my_tank.category_1()
    my_tank.category_2()
    my_tank.category_3()
    my_tank.final_calculation()
