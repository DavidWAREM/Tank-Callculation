import pandas as pd
import numpy as np


Verbrauch = pd.read_excel(r'data\Verbrauch_2019_hourly_Sample_Data.xlsx', sheet_name='temp')
df = pd.DataFrame(Verbrauch, columns=['outflow'])
#print(df)

Verbrauch_list = df.values.tolist()


Inflow = pd.read_excel(r'data\Inflow_2019_hourly_Sample_Data.xlsx', sheet_name='temp')
df = pd.DataFrame(Inflow, columns=['inflow'])
#print(df)

Verbrauch_list = df.values.tolist()




#print(product_list)
#line_data = []
#line_data.append(np.float(df))
#print(line_data)
