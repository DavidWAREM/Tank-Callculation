
V_equ = 500

area=input("Is the supplied area a residual (1), a comercial (2) or a industrial (3) area?"
              "\n Write the number ")
print(area)

if area == "1":
    floors_number=input("What is the maximum number of floors in the area?")
    floors_number=int(floors_number)
    if floors_number <= 3:

        spread_risk=input("Is the risk of fire spread small, medium or high?"
                     "\nIf you do not know, ask the responsible fire department.")
        if spread_risk == "small":
            print ("niedrig, small, Residual")
            V_fire = 2*48
        if spread_risk == "medium":
            print("niedrig, medium, Residual")
            V_fire = 2*96
        if spread_risk == "high":
            print("niedrig, high, Residual")
            V_fire = 2*96
        if spread_risk != "small" and spread_risk != "medium" and spread_risk != "high":
            print("Wrong input!")


    else:
        print("hoch Residual")
        V_fire = 2*96

if area == "2":
    floors_number = input("What is the maximum number of floors in the area?")
    floors_number = int(floors_number)
    if floors_number <= 1:
        print("niedrig Comercial")
        V_fire = 2 * 48
    else:
        print("hoch Comercial")
        V_fire = 2 * 96


if area == "3":
    print("Industrial")
    V_fire = 2 * 96

if area != "1" and area != "2" and area != "3":
    print("Input wrong")


V_st = V_equ + V_fire

print(V_st)