import pandas as pd
import numpy as np


Verbrauch = pd.read_excel(r'data\Verbrauch_2019_hourly_Sample_Data.xlsx', sheet_name='temp')
df_Verbrauch = pd.DataFrame(Verbrauch, columns=['outflow'])
#print(df)

Verbrauch_list = df_Verbrauch.values.tolist()


Inflow = pd.read_excel(r'data\Inflow_2019_hourly_Sample_Data.xlsx', sheet_name='temp')
df_inflow = pd.DataFrame(Inflow, columns=['inflow'])

inflow_list = df_inflow.values.tolist()

inflow_list1 = inflow_list[0]
inflow_list2 = inflow_list1[0]

Verbrauch_list1 = Verbrauch_list[0]
Verbrauch_list2 = Verbrauch_list1[0]

item = Inflo

"""
length = len(inflow_list)

for i in range(0, length):
    array1 = np.array(inflow_list[i])
    array2 = np.array(Verbrauch_list[i])
    array = np.array
    array = np.append(array, array1)

print(array)
"""

#    subtracted_array = np.array(np.subtract(array1, array2))



#subtracted = list(subtracted_array)

#print(subtracted)
#print(subtracted_array)


#print(inflow_list)
#print(Verbrauch_list)

#subtracted = list()
#for item1, item2 in zip(inflow_list[0], Verbrauch_list[0]):
#    subtracted.append(item1 - item2)

#print(subtracted)

#print(product_list)
#line_data = []
#line_data.append(np.float(df))
#print(line_data)
