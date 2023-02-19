# Importing Pandas to use Dataframe and Parse Excel Sheets
import pandas as panda

def run():
    # Import Raw Data from Excel Sheets using Dataframe, Repeat for all years 
    data_2014 = panda.read_excel(r'D:\uni_stuttgart\python\pycharmProjects\waterTank\data\Verbrauch_2014.xlsx', index_col=0)
    data_2015 = panda.read_excel(r'D:\uni_stuttgart\python\pycharmProjects\waterTank\data\Verbrauch_2015.xlsx', index_col=0)
    data_2016 = panda.read_excel(r'D:\uni_stuttgart\python\pycharmProjects\waterTank\data\Verbrauch_2016.xlsx', index_col=0)
    data_2017 = panda.read_excel(r'D:\uni_stuttgart\python\pycharmProjects\waterTank\data\Verbrauch_2017.xlsx', index_col=0)
    data_2018 = panda.read_excel(r'D:\uni_stuttgart\python\pycharmProjects\waterTank\data\Verbrauch_2018.xlsx', index_col=0)
    data_2019 = panda.read_excel(r'D:\uni_stuttgart\python\pycharmProjects\waterTank\data\Verbrauch_2019.xlsx', index_col=0)
    
    # The Excel Sheets have two Columns- Datum and Verbrauch
    # Now we shall find the Maximum Value from Verbrauch Column for each year 
    data_2014_df_verbrauch_max = data_2014['Verbrauch'].max()
    data_2015_df_verbrauch_max = data_2015['Verbrauch'].max()
    data_2016_df_verbrauch_max = data_2016['Verbrauch'].max()
    data_2017_df_verbrauch_max = data_2017['Verbrauch'].max()
    data_2018_df_verbrauch_max = data_2018['Verbrauch'].max()
    data_2019_df_verbrauch_max = data_2019['Verbrauch'].max()

    # Create an Array of list Containing all Maximum Values from above
    my_data = list()
    my_data.append(data_2014_df_verbrauch_max)
    my_data.append(data_2015_df_verbrauch_max)
    my_data.append(data_2016_df_verbrauch_max)
    my_data.append(data_2017_df_verbrauch_max)
    my_data.append(data_2018_df_verbrauch_max)
    my_data.append(data_2019_df_verbrauch_max)
 
    # Find Maximum Value from all years for Discharge 
    Qdmax= max(my_data)
 
    # First Criteria
    criteria_1 = 0.5 * Qdmax
    print(f"{criteria_1=}")


if __name__ == '__main__':
    run()


