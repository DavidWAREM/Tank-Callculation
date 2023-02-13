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
            print("Wrong Input, that is not one of the given options.")
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
                print("Wrong input, this is not a number!")
                continue
            else:
                break

        # If the number of floors is below 4.
        if floors_number <= 3:
            # Getting the risks of a fire spread
            spread_risk = input("Is the risk of fire spread in the area small, medium or high?"
                                "\nIf you do not know, ask the responsible fire department. ")

            # The while funktion checks, if the input is correct.
            while spread_risk != "small" and spread_risk != "medium" and spread_risk != "high":
                spread_risk = input("This is neather 'small', 'medium', or 'high'."
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
            if spread_risk != "small" and spread_risk != "medium" and spread_risk != "high":
                print("Wrong input spread risk!")

        # If The number of floors is more than 3.
        else:
            spread_risk = input("Is the risk of fire spread in the area small, medium or high?"
                                "\nIf you do not know, ask the responsible fire department. ")

            while spread_risk != "small" and spread_risk != "medium" and spread_risk != "high":
                spread_risk = input("This is neather 'small', 'medium', or 'high'."
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
                print("Wrong input, this is not a number!")
                continue
            else:
                break

        if floors_number <= 1:
            spread_risk = input("Is the risk of fire spread in the area small, medium or high?"
                                "\nIf you do not know, ask the responsible fire department. ")

            while spread_risk != "small" and spread_risk != "medium" and spread_risk != "high":
                spread_risk = input("This is neather 'small', 'medium', or 'high'."
                                    "\nPlease check the risk of fire spread and insert on of the three terms. ")

            if spread_risk == "small":
                print("niedrig, small, Comercial")
                V_fire = 2 * 96
            if spread_risk == "medium":
                print("niedrig, medium, Comercial")
                V_fire = 2 * 96
            if spread_risk == "high":
                print("niedrig, high, Comercial")
                V_fire = 2 * 192
            if spread_risk != "small" and spread_risk != "medium" and spread_risk != "high":
                print("Wrong input spread risk!")
        else:
            spread_risk = input("Is the risk of fire spread in the area small, medium or high?"
                                "\nIf you do not know, ask the responsible fire department. ")

            while spread_risk != "small" and spread_risk != "medium" and spread_risk != "high":
                spread_risk = input("This is neather 'small', 'medium', or 'high'."
                                    "\nPlease check the risk of fire spread and insert on of the three terms. ")

            if spread_risk == "small":
                print("hoch, small, Comercial")
                V_fire = 2 * 96
            if spread_risk == "medium":
                print("hoch, medium, Comercial")
                V_fire = 2 * 192
            if spread_risk == "high":
                print("hoch, high, Comercial")
                V_fire = 2 * 192
            if spread_risk != "small" and spread_risk != "medium" and spread_risk != "high":
                print("Wrong input spread risk!")

    # If it is a industrial area, this is the branche.
    if area == 3:

        spread_risk = input("Is the risk of fire spread in the area small, medium or high?"
                            "\nIf you do not know, ask the responsible fire department. ")

        while spread_risk != "small" and spread_risk != "medium" and spread_risk != "high":
            spread_risk = input("This is neather 'small', 'medium', or 'high'."
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
        if spread_risk != "small" and spread_risk != "medium" and spread_risk != "high":
            print("Wrong input spread risk!")

    V_st = V_equ + V_fire

    print(V_st)


category_2()
