import logging
import pandas as panda
from fun import *
from Category import Tank

if __name__ == '__main__':
    start_logging()
    my_tank = Tank()
    my_tank.tank_data()
    my_tank.category_1()
    my_tank.category_2()
    my_tank.category_3()
    my_tank.final_calculation()
