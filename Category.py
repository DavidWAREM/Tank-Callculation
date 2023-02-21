from fun import *
import pandas as pd
from main import run



# Beginning Definition of daily amount of water, this will be later delited.
V_equ = 500

"""
Category_2 calculates the additional amount of water required for a case of a fire. 
The calculation is based on three criteria: First the type of area, that is supplied
(residual, commercial or industrial), second the highest building in the area (number of floors),
and third the risk of fire spread (small, medium and high). 
"""


def category_1():
    # Import Raw Data from Excel Sheets using Dataframe, Repeat for all years 
    data_2014 = panda.read_excel(r"data\Verbrauch_2014.xlsx", index_col=0)
    data_2015 = panda.read_excel(r"data\Verbrauch_2015.xlsx", index_col=0)
    data_2016 = panda.read_excel(r"data\Verbrauch_2016.xlsx", index_col=0)
    data_2017 = panda.read_excel(r"data\Verbrauch_2017.xlsx", index_col=0)
    data_2018 = panda.read_excel(r"data\Verbrauch_2018.xlsx", index_col=0)
    data_2019 = panda.read_excel(r"data\Verbrauch_2019.xlsx", index_col=0)
    logging.info("The outflow data are properly loaded into the system.")

    data = list()
    data.append(data_2014)
    data.append(data_2015)
    data.append(data_2016)
    data.append(data_2017)
    data.append(data_2018)
    data.append(data_2019)
  
    # The Excel Sheets have two Columns- Datum and Verbrauch
    # Now we shall find the Maximum Value from Verbrauch Column for each year
    data_2014_df_verbrauch_max = data_2014['Verbrauch'].max()
    data_2015_df_verbrauch_max = data_2015['Verbrauch'].max()
    data_2016_df_verbrauch_max = data_2016['Verbrauch'].max()
    data_2017_df_verbrauch_max = data_2017['Verbrauch'].max()
    data_2018_df_verbrauch_max = data_2018['Verbrauch'].max()
    data_2019_df_verbrauch_max = data_2019['Verbrauch'].max()
 
    # Create an Array of list Containing all Maximum Values from above
    my_data = list()
    my_data.append(data_2014_df_verbrauch_max)
    my_data.append(data_2015_df_verbrauch_max)
    my_data.append(data_2016_df_verbrauch_max)
    my_data.append(data_2017_df_verbrauch_max)
    my_data.append(data_2018_df_verbrauch_max)
    my_data.append(data_2019_df_verbrauch_max)
    
    # Find Maximum Value from all years for Discharge
    qdmax= max(my_data)
    logging.info(f"The max. amount of outflow is {qdmax}.")
   
    # First Criteria
    criteria_1 = 0.5 * qdmax
    print(f"{criteria_1=}")
    logging.info(f"The category 1 is {criteria_1}.")


def category_2():

    # the while True checks, if the input is correct
    print("Is the supplied area a residual (1), a commercial (2) or a industrial (3) area?")
    while True:
        try:
            area = int(input("Please insert 1 for residual, 2 for commercial and 3 for industrial area: "))
        except ValueError:
            print("Wrong input, that is not one of the given options.")
            logging.exception("User input for area is not a number.")
            continue
        else:
            break

    # Checks if the input is not 0
    while area == 0:
        print("Wrong input, that is not one of the given options.")
        logging.error("User input for area == 0.")
        while True:
            try:
                area = int(input("Please insert 1 for residual, 2 for commercial and 3 for industrial area: "))
            except ValueError:
                print("Wrong input, that is not one of the given options.")
                logging.exception("User input for area is not a number.")
                continue
            else:
                break

    # Checks if the input is not higher than 3
    while area >= 4:
        print("Wrong input, that is not one of the given options.")
        logging.error("User input for area >= 4.")
        while True:
            try:
                area = int(input("Please insert 1 for residual, 2 for commercial and 3 for industrial area: "))
            except ValueError:
                print("Wrong input, that is not one of the given options.")
                logging.exception("User input for area is not a number.")
                continue
            else:
                break

    if area == 1:
        # If the area is a Residual, this is the branche.
        # The while True checks, is the input for the floor number is correct.
        print("What is the maximum number of floors in the area? ")
        while True:
            try:
                floors_number = int(input("Please insert a number: "))
            except ValueError:
                print("Wrong input!")
                logging.exception("User input for floor is not a number.")
                continue
            else:
                break

        # Checks if the floor number is not '0'.
        while floors_number == 0:
            print("Wrong input, if the floor number is '0', there would be no building.")
            logging.error("User input for floor number == 0.")
            while True:
                try:
                    floors_number = int(input("Please insert a number: "))
                except ValueError:
                    print("Wrong input!")
                    logging.exception("User input for floor number is not a number.")
                    continue
                else:
                    break

        # If the number of floors is between 1 and 3.
        if floors_number <= 3:
            # Getting the risks of a fire spread
            spread_risk = input("Is the risk of fire spread in the area small, medium or high?"
                                "\nIf you do not know, ask the responsible fire department. ")

            # The while funktion checks, if the input is correct.
            while spread_risk != "small" and spread_risk != "medium" and spread_risk != "high":
                spread_risk = input("This is neither 'small', 'medium', or 'high'."
                                    "\nPlease check the risk of fire spread and insert on of the three terms. ")
                logging.error("The input for the fire risk is neither small, medium or high.")

            if spread_risk == "small":
                print("niedrig, small, Residual")
                V_fire = 2 * 48
            if spread_risk == "medium":
                print("niedrig, medium, Residual")
                V_fire = 2 * 96
            if spread_risk == "high":
                print("niedrig, high, Residual")
                V_fire = 2 * 96

        # If The number of floors is more than 3.
        else:
            spread_risk = input("Is the risk of fire spread in the area small, medium or high?"
                                "\nIf you do not know, ask the responsible fire department. ")

            while spread_risk != "small" and spread_risk != "medium" and spread_risk != "high":
                spread_risk = input("This is neither 'small', 'medium', or 'high'."
                                    "\nPlease check the risk of fire spread and insert on of the three terms. ")
                logging.error("The input for the fire risk is neither small, medium or high.")

            if spread_risk == "small":
                print("hoch, small, Residual")
                V_fire = 2 * 96
            if spread_risk == "medium":
                print("hoch, medium, Residual")
                V_fire = 2 * 96
            if spread_risk == "high":
                print("hoch, high, Residual")
                V_fire = 2 * 192

    # If it is a commercial area, this is the branche.
    if area == 2:
        # Again the while True checks, if the input is correct.
        print("What is the maximum number of floors in the area? ")
        while True:
            try:
                floors_number = int(input("Please insert a number: "))
            except ValueError:
                print("Wrong input!")
                logging.exception("User input for floor number is not a number.")
                continue
            else:
                break

        # Checks if the floor number is not '0'.
        while floors_number == 0:
            print("Wrong input, if the floor number is '0', there would be no building.")
            logging.error("Input for floor number == 0.")
            while True:
                try:
                    floors_number = int(input("Please insert a number: "))
                except ValueError:
                    print("Wrong input!")
                    logging.exception("User input for floor number is not a number.")
                    continue
                else:
                    break

        if floors_number <= 1:
            spread_risk = input("Is the risk of fire spread in the area small, medium or high?"
                                "\nIf you do not know, ask the responsible fire department. ")

            while spread_risk != "small" and spread_risk != "medium" and spread_risk != "high":
                spread_risk = input("This is neither 'small', 'medium', or 'high'."
                                    "\nPlease check the risk of fire spread and insert on of the three terms. ")
                logging.error("The input for the fire risk is neither small, medium or high.")

            if spread_risk == "small":
                print("niedrig, small, Commercial")
                V_fire = 2 * 96
            if spread_risk == "medium":
                print("niedrig, medium, Commercial")
                V_fire = 2 * 96
            if spread_risk == "high":
                print("niedrig, high, Commercial")
                V_fire = 2 * 192

        else:
            spread_risk = input("Is the risk of fire spread in the area small, medium or high?"
                                "\nIf you do not know, ask the responsible fire department. ")

            while spread_risk != "small" and spread_risk != "medium" and spread_risk != "high":
                spread_risk = input("This is neither 'small', 'medium', or 'high'."
                                    "\nPlease check the risk of fire spread and insert on of the three terms. ")
                logging.error("The input for the fire risk is neither small, medium or high.")

            if spread_risk == "small":
                print("hoch, small, Commercial")
                V_fire = 2 * 96
            if spread_risk == "medium":
                print("hoch, medium, Commercial")
                V_fire = 2 * 192
            if spread_risk == "high":
                print("hoch, high, Commercial")
                V_fire = 2 * 192

    # If it is an industrial area, this is the branche.
    if area == 3:

        spread_risk = input("Is the risk of fire spread in the area small, medium or high?"
                            "\nIf you do not know, ask the responsible fire department. ")

        while spread_risk != "small" and spread_risk != "medium" and spread_risk != "high":
            spread_risk = input("This is neither 'small', 'medium', or 'high'."
                                "\nPlease check the risk of fire spread and insert on of the three terms. ")
            logging.error("The input for the fire risk is neither small, medium or high.")

        if spread_risk == "small":
            print("small, Industrial")
            V_fire = 2 * 96
        if spread_risk == "medium":
            print("medium, Industrial")
            V_fire = 2 * 192
        if spread_risk == "high":
            print("high, Industrial")
            V_fire = 2 * 192

    logging.info(f"The user input for the area is a {area}.")

    while True:
        try:
            logging.info(f"The user input for the floor numbers is {floors_number}.")
        except UnboundLocalError:
            continue
        else:
            break

    logging.info(f"The user input for the risk of a fire spread is {spread_risk}.")


    V_st = V_equ + V_fire

    print(V_st)


def category_3():

    print("The following step will calculate category three. "
          "Here, it is checked whether a minimum height of 0.5 meters"
          " of water column was always present in the course of the given tank.")

    # The following will ask the size of the tank from the user.
    while True:
        try:
            length = int(input("Please insert the length of the tank. "))
        except ValueError:
            print("Wrong input.")
            logging.exception("The input for the tank length is wrong.")
            continue
        else:
            break

    while True:
        try:
            width = int(input("Please insert the width of the tank. "))
        except ValueError:
            print("Wrong input.")
            logging.exception("The input for the tank width is wrong.")
            continue
        else:
            break

    floor_area = width * length
    print(floor_area)

    logging.info(f"The input for the width is {width}.")
    logging.info(f"The input for the length is {length}.")
    logging.info(f"The calculated area for the tank is {floor_area}.")

    # Here the hourly inflow and outflow data will be imported to python.
    df_outflow_2018 = pd.read_excel('data\Verbrauch_2018_hourly_Sample_Data.xlsx', sheet_name='temp')
    df_outflow_2019 = pd.read_excel('data\Verbrauch_2019_hourly_Sample_Data.xlsx', sheet_name='temp')
    logging.info("The hourly outflow data are properly loaded into the system.")

    df_inflow_2018 = pd.read_excel('data\Inflow_2018_hourly_Sample_Data.xlsx', sheet_name='temp')
    df_inflow_2019 = pd.read_excel('data\Inflow_2019_hourly_Sample_Data.xlsx', sheet_name='temp')
    logging.info("The hourly inflow data are properly loaded into the system.")

    # The starting point of the water hight (df) and the water_column_counter is 0.
    df = 0
    water_column_counter = 0

    # The for function will work with every row of the data. At every moment it will
    # calculate the water hight. If the water hight is below 0.5 meters, there will be a massage
    # and a 1 will be added to the water column counter.
    for index, row in df_inflow_2018.iterrows():
        df_1 = df_inflow_2018.at[index, "inflow"]
        df_2 = df_outflow_2018.at[index, "outflow"]
        df = df_1 - df_2 + df
        water_column = df / floor_area
        if water_column <= 0.5:
            print("At the moment {} was the water column below 0.5 meter.".format(df_inflow_2019.at[index, "date"]))
            print("The water column had a height of {} meter.".format(water_column))
            print("The water had a volume of {} liters.".format(df))
            water_column_counter = water_column_counter + 1
            logging.info("At the moment {} the water column was to small"
                         " and had a height of {}.".format(df_inflow_2019.at[index, "date"], water_column))

    for index, row in df_inflow_2019.iterrows():
        df_1 = df_inflow_2019.at[index, "inflow"]
        df_2 = df_outflow_2019.at[index, "outflow"]
        df = df_1 - df_2 + df
        water_column = df / floor_area
        if water_column <= 0.5:
            print("At the moment {} was the water column below 0.5 meter.".format(df_inflow_2019.at[index, "date"]))
            print("The water column had a hight of {} meter.".format(water_column))
            print("The water had a volume of {} liters.".format(df))
            water_column_counter = water_column_counter + 1
            logging.info("At the moment {} the water column was to small"
                         " and had a height of {}.".format(df_inflow_2018.at[index, "date"], water_column))

    # If the water colum counter is 0, and therefore the water column hight was always
    # above 0.5 meter, this massage will be showen to the user.
    if water_column_counter <= 1:
        print("The water column is always above 0.5 meters.")
        logging.info("Category 3 is fulfilled, the water height was never below 0.5 meters.")



#category_2()

#category_3()
