from typing import List

import pandas as pd

def category_3():
    """
    print("The following step will calculate criterion three. "
          "Here, it is checked whether a minimum height of 0.5 meters"
          " of water column was always present in the course of the given tank.")

    #The following will ask the size of the tank from the user.
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





    filename = 'test.txt'

    with open (filename) as file_object:
        asdf = file_object.readlines()

    data = ''
    for line in asdf:
        data += line.strip()

    print(data)
    print(len(data))
"""

Verbrauch_gesammt = pd.read_excel(r'data\Verbrauch_2019-hourly_Sampel Data.xlsx')
Verbrauch = pd.DataFrame(Verbrauch_gesammt, columns=["Verbrauch"])

data_Verbrauch = ""
data_Verbrauch = Verbrauch.values.tolist()

#print(data_Verbrauch)

Inflow_gesammt = pd.read_excel(r'data\Inflow_2019-hourly_Sampel Data.xlsx')
Inflow = pd.DataFrame(Inflow_gesammt, columns=["Inflow"])

data_Inflow = ""
data_Inflow = Inflow.values.tolist()

#print(data_Inflow)

for i in data_Inflow:
    try:
        int(i)
    except ValueError:






#for i, j in zip(list1, list2):
#    result.append(i - j)
#print(result)


category_3()
