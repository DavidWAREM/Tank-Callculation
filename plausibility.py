import pandas as panda
import numpy as npy

data = panda.read_excel(r'C:\Users\lusti\Documents\GitHub\Tank-Callculation\data\Verbrauch_2014.xlsx')

data_verbrauch_max = data['Verbrauch'].max()
date_consumption_max = data['Datum'][data['Verbrauch'] == data_verbrauch_max]

#if date_consumption_max = ""
#data["Datum"] = data[date_consumption_max].dt.month

#print(var)

#test

print(data_verbrauch_max)
print(date_consumption_max)
#print(date_consumption_max.month)
#print(data['Datum'][data['Verbrauch'] == data_verbrauch_max])


