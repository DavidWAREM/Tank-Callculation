import logging

import pandas as pd
from fun import *



class Tank:
    """
    This class inherent the algorithm for the calculation.
    """

    def __init__(self):
        """Initialise attributes."""
        self.length = 0
        self.width = 0
        self.floor_area = 0
        self.volume = 0
        self.qdmax = 0
        self.criteria_1 = 0
        self.criteria_2 = 0
        self.criteria_3 = 0

    def tank_data(self):
        print("\nFirst you need to name the size of your tank.")

        # The following will ask the size of the tank from the user.
        while True:
            try:
                self.length = int(input("Please insert the length of the tank in meter. "))
            except ValueError:
                print("Wrong input.")
                logging.exception("The input for the tank length is wrong.")
                continue
            else:
                break

        while self.length <= 0:
            print("Wrong input, the length can not be 0 or less.")
            logging.error("User input for length <= 0.")
            while True:
                try:
                    self.length = int(input("Please insert the length of the tank in meter. "))
                except ValueError:
                    print("Wrong input.")
                    logging.exception("The input for the tank length is wrong.")
                    continue
                else:
                    break

        logging.info(f"The user input for the length is {self.length}.")

        while True:
            try:
                self.width = int(input("Please insert the width of the tank in meter. "))
            except ValueError:
                print("Wrong input.")
                logging.exception("The input for the tank width is wrong.")
                continue
            else:
                break

        while self.width <= 0:
            print("Wrong input, the width can not be 0 or less.")
            logging.error("User input for width <= 0.")
            while True:
                try:
                    self.width = int(input("Please insert the width of the tank in meter. "))
                except ValueError:
                    print("Wrong input.")
                    logging.exception("The input for the tank width is wrong.")
                    continue
                else:
                    break

        logging.info(f"The user input for the width is {self.width}.")

        self.floor_area = self.width * self.length
        logging.info(f"The calculated area for the tank is {self.floor_area} m^2.")

        while True:
            try:
                self.volume = int(input("Please insert the volume of the tank in cubic meter. "))
            except ValueError:
                print("Wrong input.")
                logging.exception("The input for the tank volume is wrong.")
                continue
            else:
                break

        while self.volume <= 0:
            print("Wrong input, the volume can not be 0 or less.")
            logging.error("User input for volume <= 0.")
            while True:
                try:
                    self.volume = int(input("Please insert the volume of the tank in cubic meter. "))
                except ValueError:
                    print("Wrong input.")
                    logging.exception("The input for the tank volume is wrong.")
                    continue
                else:
                    break

        logging.info(f"The user input for the volume of the tank is {self.volume}.")

    def category_1(self):
        # Import the Data after the plausibility check from Excel Sheets using Dataframe, Repeat for all years
        data_2014 = pd.read_excel(r'data\\Plausible_Consumption_2014.xlsx')
        data_2015 = pd.read_excel(r'data\\Plausible_Consumption_2015.xlsx')
        data_2016 = pd.read_excel(r'data\\Plausible_Consumption_2016.xlsx')
        data_2017 = pd.read_excel(r'data\\Plausible_Consumption_2017.xlsx')
        data_2018 = pd.read_excel(r'data\\Plausible_Consumption_2018.xlsx')
        data_2019 = pd.read_excel(r'data\\Plausible_Consumption_2019.xlsx')
        logging.info("The outflow data are properly loaded into the system.")

        data = list()
        data.append(data_2014)
        data.append(data_2015)
        data.append(data_2016)
        data.append(data_2017)
        data.append(data_2018)
        data.append(data_2019)

        # The Excel Sheets have two Columns - Date and Consumption
        # Now we shall find the Maximum Value from Consumption Column for each year
        data_2014_df_cons_max = data_2014['Consumption'].max()
        data_2015_df_cons_max = data_2015['Consumption'].max()
        data_2016_df_cons_max = data_2016['Consumption'].max()
        data_2017_df_cons_max = data_2017['Consumption'].max()
        data_2018_df_cons_max = data_2018['Consumption'].max()
        data_2019_df_cons_max = data_2019['Consumption'].max()

        # Create an Array of list Containing all Maximum Values from above
        my_data = list()
        my_data.append(data_2014_df_cons_max)
        my_data.append(data_2015_df_cons_max)
        my_data.append(data_2016_df_cons_max)
        my_data.append(data_2017_df_cons_max)
        my_data.append(data_2018_df_cons_max)
        my_data.append(data_2019_df_cons_max)

        # Find Maximum Value from all years for Discharge
        self.qdmax = max(my_data)
        logging.info(f"The max. amount of outflow is {self.qdmax}.")

        # First Criteria
        # The tank should have the volume of the water needed on
        # day with the highest consumption for the howl day.
        self.criteria_1 = 0.5 * self.qdmax
        print(f"Criteria 1 = {self.criteria_1} m^3")
        logging.info(f"The category 1 is {self.criteria_1}.")

    def category_2(self):
        # the while True checks, if the input is correct
        area = 0
        print('Is the supplied area a residual (1), a commercial (2) or a industrial (3) area?')
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
            # If the area is a Residual, this is the branch.
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
                logging.info(f"The user input for floors number is {floors_number}.")
                # Getting the risks of a fire spread
                spread_risk = input("Is the risk of fire spread in the area small, medium or high?"
                                    "\nIf you do not know, ask the responsible fire department. ")

                # The while funktion checks, if the input is correct.
                while spread_risk != "small" and spread_risk != "medium" and spread_risk != "high":
                    spread_risk = input("This is neither 'small', 'medium', or 'high'."
                                        "\nPlease check the risk of fire spread and insert on of the three terms. ")
                    logging.error("The input for the fire risk is neither small, medium or high.")

                if spread_risk == "small":
                    v_fire = 2 * 48
                if spread_risk == "medium":
                    v_fire = 2 * 96
                if spread_risk == "high":
                    v_fire = 2 * 96

            # If The number of floors is more than 3.
            else:
                logging.info(f"The user input for floors number is {floors_number}.")
                spread_risk = input("Is the risk of fire spread in the area small, medium or high?"
                                    "\nIf you do not know, ask the responsible fire department. ")

                while spread_risk != "small" and spread_risk != "medium" and spread_risk != "high":
                    spread_risk = input("This is neither 'small', 'medium', or 'high'."
                                        "\nPlease check the risk of fire spread and insert on of the three terms. ")
                    logging.error("The input for the fire risk is neither small, medium or high.")

                if spread_risk == "small":
                    v_fire = 2 * 96
                if spread_risk == "medium":
                    v_fire = 2 * 96
                if spread_risk == "high":
                    v_fire = 2 * 192

        # If it is a commercial area, this is the branch.
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
                logging.info(f"The user input for floors number is {floors_number}.")
                spread_risk = input("Is the risk of fire spread in the area small, medium or high?"
                                    "\nIf you do not know, ask the responsible fire department. ")

                while spread_risk != "small" and spread_risk != "medium" and spread_risk != "high":
                    spread_risk = input("This is neither 'small', 'medium', or 'high'."
                                        "\nPlease check the risk of fire spread and insert on of the three terms. ")
                    logging.error("The input for the fire risk is neither small, medium or high.")

                if spread_risk == "small":
                    v_fire = 2 * 96
                if spread_risk == "medium":
                    v_fire = 2 * 96
                if spread_risk == "high":
                    v_fire = 2 * 192

            else:
                logging.info(f"The user input for floors number is {floors_number}.")
                spread_risk = input("Is the risk of fire spread in the area small, medium or high?"
                                    "\nIf you do not know, ask the responsible fire department. ")

                while spread_risk != "small" and spread_risk != "medium" and spread_risk != "high":
                    spread_risk = input("This is neither 'small', 'medium', or 'high'."
                                        "\nPlease check the risk of fire spread and insert on of the three terms. ")
                    logging.error("The input for the fire risk is neither small, medium or high.")

                if spread_risk == "small":
                    v_fire = 2 * 96
                if spread_risk == "medium":
                    v_fire = 2 * 192
                if spread_risk == "high":
                    v_fire = 2 * 192

        # If it is an industrial area, this is the branch.
        if area == 3:

            spread_risk = input("Is the risk of fire spread in the area small, medium or high?"
                                "\nIf you do not know, ask the responsible fire department. ")

            while spread_risk != "small" and spread_risk != "medium" and spread_risk != "high":
                spread_risk = input("This is neither 'small', 'medium', or 'high'."
                                    "\nPlease check the risk of fire spread and insert on of the three terms. ")
                logging.error("The input for the fire risk is neither small, medium or high.")

            if spread_risk == "small":
                v_fire = 2 * 96
            if spread_risk == "medium":
                v_fire = 2 * 192
            if spread_risk == "high":
                v_fire = 2 * 192

        logging.info(f"The user input for the area is a {area}.")
        logging.info(f"The user input for the risk of a fire spread is {spread_risk}.")

        """The Category 2 is calculated by the amount for the firefighter plus qdmax * 0.3."""
        self.criteria_2 = v_fire + 0.3 * self.qdmax
        print(f"Criteria 2 = {self.criteria_2} m^3.")

    def category_3(self):

        # Here the hourly inflow and outflow data will be imported to python.
        df_outflow_2018 = pd.read_excel('data\\Verbrauch_2018_hourly.xlsx')
        df_outflow_2019 = pd.read_excel('data\\Verbrauch_2019_hourly.xlsx')
        logging.info("The hourly outflow data are properly loaded into the system.")

        df_inflow_2018 = pd.read_excel('data\\Inflow_2018_hourly.xlsx')
        df_inflow_2019 = pd.read_excel('data\\Inflow_2019_hourly.xlsx')
        logging.info("The hourly inflow data are properly loaded into the system.")

        # The for function will work with every row of the data. At every moment it will
        # calculate the difference between inflow and outflow.
        # The biggest value plus the minimum Volume to maintain the 0.5 meters in the tank is the criteria 2.
        list_df = []
        for index, row in df_inflow_2018.iterrows():
            df_1 = df_inflow_2018.at[index, "inflow"]
            df_2 = df_outflow_2018.at[index, "outflow"]
            df = df_2 - df_1
            list_df.append(df)

        for index, row in df_inflow_2019.iterrows():
            df_1 = df_inflow_2019.at[index, "inflow"]
            df_2 = df_outflow_2019.at[index, "outflow"]
            df = df_2 - df_1
            list_df.append(df)

        q_fluc = max(list_df)
        q_min = self.floor_area * 0.5
        self.criteria_3 = q_fluc + q_min
        logging.info(f"The q_fluc is {q_fluc} m^3.")
        logging.info(f"The q_min is {q_min} m^3.")
        logging.info(f"The criteria_3 is {self.criteria_3} m^3.")
        print(f"The criteria 3 is {self.criteria_3} m^3.")

    def final_calculation(self):
        criteria = {"Category 1, qdmax": self.criteria_1,
                    "Category 2, additional water for firefighters": self.criteria_2,
                    "Criteria 3, volume needed to maintain a minimum water level in the water tank": self.criteria_3}
        criteria_max = max(self.criteria_1, self.criteria_2, self.criteria_3)
        if criteria_max <= self.volume:
            print("The given tank is big enough for the given situation."
                  f"\nThe minimum tank volume would be {criteria_max} m^3 from {max(criteria)}.")
            logging.info("The given tank is big enough.")
        else:
            print("The given tank is not big enough for the given situation."
                  f"\nThe given volume was {self.volume} m^3.")
            print(f"The needed volume regarding this situation would be {criteria_max} m^3 from {max(criteria)}.")
            logging.info("The given tank is not big enough for the given situation.")
            logging.info(f"The needed volume regarding this situation would be {criteria_max} m^3 from {max(criteria)}.")

