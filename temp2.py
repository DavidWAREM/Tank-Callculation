import pandas as pd




floor_area = 30

df_outflow_2018 = pd.read_excel('data\Verbrauch_2018_hourly_Sample_Data.xlsx', sheet_name='temp')
df_outflow_2019 = pd.read_excel('data\Verbrauch_2019_hourly_Sample_Data.xlsx', sheet_name='temp')

df_inflow_2018 = pd.read_excel('data\Inflow_2018_hourly_Sample_Data.xlsx', sheet_name='temp')
df_inflow_2019 = pd.read_excel('data\Inflow_2019_hourly_Sample_Data.xlsx', sheet_name='temp')

df = 0

for index, row in df_inflow_2018.iterrows():
    df_1 = df_inflow_2018.at[index, "inflow"]
    df_2 = df_outflow_2018.at[index, "outflow"]
    df = df_1 - df_2 + df
    water_column = df / floor_area
    if water_column <= 0.5:
        print("Zu dieser Zeit war die Wassersäule unter 0.5 Meter.")
        print(df_inflow_2018.at[index, "date"])
        print(water_column)
        print(df)


for index, row in df_inflow_2019.iterrows():
    df_1 = df_inflow_2019.at[index, "inflow"]
    df_2 = df_outflow_2019.at[index, "outflow"]
    df = df_1 - df_2 + df
    water_column = df / floor_area
    if water_column <= 0.5:
        print("Zu dieser Zeit war die Wassersäule unter 0.5 Meter.")
        print(df_inflow_2019.at[index, "date"])
        print(water_column)
        print(df)