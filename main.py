import pandas as pd
from plausibility import Plausibility, PlotDaily
from fun import *
from category import Tank

# Import raw data from the Excel sheets for each year
data_raw_2017 = pd.read_excel(r'data\\Consumption_2017.xlsx')
data_raw_2018 = pd.read_excel(r'data\\Consumption_2018.xlsx')
data_raw_2019 = pd.read_excel(r'data\\Consumption_2019.xlsx')


print("This algorithm will calculate, if the given tank is big enough for the given outflow data,"
      "\nregarding the German law for water supply facilities.")

if __name__ == '__main__':
    start_logging()

    p_2017 = Plausibility(data_raw_2017, "2017")
    pl_2017 = PlotDaily(data_raw_2017, "2017")
    p_2018 = Plausibility(data_raw_2018, "2018")
    pl_2018 = PlotDaily(data_raw_2018, "2018")
    p_2019 = Plausibility(data_raw_2019, "2019")
    pl_2019 = PlotDaily(data_raw_2019, "2019")
    pl_2017.plot_daily()
    p_2017.check_plausibility()
    pl_2018.plot_daily()
    p_2018.check_plausibility()
    pl_2019.plot_daily()
    p_2019.check_plausibility()

    my_tank = Tank()
    my_tank.tank_data()
    my_tank.category_1()
    my_tank.category_2()
    my_tank.category_3()
    my_tank.final_calculation()
