# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as panda

def find_qdmax(df):
    pass

def run():
    data_2014 = panda.read_excel(r'D:\uni_stuttgart\python\pycharmProjects\waterTank\data\Verbrauch_2014.xlsx', index_col=0)
    data_2015 = panda.read_excel(r'D:\uni_stuttgart\python\pycharmProjects\waterTank\data\Verbrauch_2015.xlsx', index_col=0)
    data_2016 = panda.read_excel(r'D:\uni_stuttgart\python\pycharmProjects\waterTank\data\Verbrauch_2016.xlsx', index_col=0)
    data_2017 = panda.read_excel(r'D:\uni_stuttgart\python\pycharmProjects\waterTank\data\Verbrauch_2017.xlsx', index_col=0)
    data_2018 = panda.read_excel(r'D:\uni_stuttgart\python\pycharmProjects\waterTank\data\Verbrauch_2018.xlsx', index_col=0)
    data_2019 = panda.read_excel(r'D:\uni_stuttgart\python\pycharmProjects\waterTank\data\Verbrauch_2019.xlsx', index_col=0)

    data = list()
    data.append(data_2014)
    data.append(data_2015)
    data.append(data_2016)
    data.append(data_2017)
    data.append(data_2018)
    data.append(data_2019)

    data_2014_df_verbrauch_max = data_2014['Verbrauch'].max()
    data_2015_df_verbrauch_max = data_2015['Verbrauch'].max()
    data_2016_df_verbrauch_max = data_2016['Verbrauch'].max()
    data_2017_df_verbrauch_max = data_2017['Verbrauch'].max()
    data_2018_df_verbrauch_max = data_2018['Verbrauch'].max()
    data_2019_df_verbrauch_max = data_2019['Verbrauch'].max()

    my_data = list()
    my_data.append(data_2014_df_verbrauch_max)
    my_data.append(data_2015_df_verbrauch_max)
    my_data.append(data_2016_df_verbrauch_max)
    my_data.append(data_2017_df_verbrauch_max)
    my_data.append(data_2018_df_verbrauch_max)
    my_data.append(data_2019_df_verbrauch_max)

    Qdmax= max(my_data)
    print(f"{Qdmax=}")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/