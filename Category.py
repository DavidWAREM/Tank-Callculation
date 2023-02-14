# Beginning Definition of daily amount of water, this will be later delited.
V_equ = 500

"""
Category_2 calculates the additional amount of water required for a case of a fire. 
The calculation is based on three criteria: First the type of area, that is supplied
(residual, commercial or industrial), second the highest building in the area (number of floors),
and third the risk of fire spread (small, medium and high). 
"""


def category_2():
    # the while True checks, if the input is correct
    print("Is the supplied area a residual (1), a commercial (2) or a industrial (3) area?")
    while True:
        try:
            area = int(input("Please insert 1 for residual, 2 for commercial and 3 for industrial area: "))
        except ValueError:
            print("Wrong input, that is not one of the given options.")
            continue
        else:
            break

    # Checks if the input is not 0
    while area == 0:
        print("Wrong input, that is not one of the given options.")
        while True:
            try:
                area = int(input("Please insert 1 for residual, 2 for commercial and 3 for industrial area: "))
            except ValueError:
                print("Wrong input, that is not one of the given options.")
                continue
            else:
                break

    # Checks if the input is not higher than 3
    while area >= 4:
        print("Wrong input, that is not one of the given options.")
        while True:
            try:
                area = int(input("Please insert 1 for residual, 2 for commercial and 3 for industrial area: "))
            except ValueError:
                print("Wrong input, that is not one of the given options.")
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
                continue
            else:
                break

        # Checks if the floor number is not '0'.
        while floors_number == 0:
            print("Wrong input, if the floor number is '0', there would be no building.")
            while True:
                try:
                    floors_number = int(input("Please insert a number: "))
                except ValueError:
                    print("Wrong input!")
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
                continue
            else:
                break

        # Checks if the floor number is not '0'.
        while floors_number == 0:
            print("Wrong input, if the floor number is '0', there would be no building.")
            while True:
                try:
                    floors_number = int(input("Please insert a number: "))
                except ValueError:
                    print("Wrong input!")
                    continue
                else:
                    break

        if floors_number <= 1:
            spread_risk = input("Is the risk of fire spread in the area small, medium or high?"
                                "\nIf you do not know, ask the responsible fire department. ")

            while spread_risk != "small" and spread_risk != "medium" and spread_risk != "high":
                spread_risk = input("This is neither 'small', 'medium', or 'high'."
                                    "\nPlease check the risk of fire spread and insert on of the three terms. ")

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

        if spread_risk == "small":
            print("small, Industrial")
            V_fire = 2 * 96
        if spread_risk == "medium":
            print("medium, Industrial")
            V_fire = 2 * 192
        if spread_risk == "high":
            print("high, Industrial")
            V_fire = 2 * 192


    V_st = V_equ + V_fire

    print(V_st)


def category_3():

    print("The following step will calculate criterion three. "
          "Here, it is checked whether a minimum height of 0.5 meters"
          " of water column was always present in the course of the given tank.")

    # The following will ask the size of the tank from the user.
    while True:
        try:
            length = int(input("Please insert the length of the tank. "))
        except ValueError:
            print("Wrong input.")
            continue
        else:
            break

    while True:
        try:
            width = int(input("Please insert the width of the tank. "))
        except ValueError:
            print("Wrong input.")
            continue
        else:
            break

    area = width * length
    print(area)

category_2()
