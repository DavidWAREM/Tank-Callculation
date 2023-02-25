import pandas as panda
import numpy as np
from PlotData import plot_data
from datetime import datetime as dt

data = panda.read_excel(r'data\Consumption_2014.xlsx')


# df = panda.DataFrame(data)
# print(data)
def plausibility(date_series=panda.Series(), consumption_series=panda.Series()):
    """

    :param date_series:
    :param consumption_series:
    :return:
    """
    data = panda.read_excel(r'data\Consumption_2014.xlsx')
    plot_data(data['Datum'], data['Verbrauch'], "Daily Consumption", "Date [year-month]", "Consumption[M3/day]", 1,
              "blue")
    data_verbrauch_max = data['Verbrauch'].max()
    date_consumption_max = data['Datum'][data['Verbrauch'] == data_verbrauch_max]
    print(date_consumption_max.to_string(index=False))
    dates = np.array(date_consumption_max)
    check1 = panda.to_datetime(dates).month
    if check1 > 5 and check1 < 10:
        print("Yuhu, Summer!!")
        print(date_consumption_max['Datum', 'Verbrauch'])
    else:
        print("Oops, pipe bursted!!")
        #data = data.drop(data['Verbrauch'] == data_verbrauch_max)
        print(date_consumption_max)


plausibility(data['Datum'], data['Verbrauch'])

"""plot_data(data['Datum'],data['Verbrauch'],"Daily Consumption",1,"blue")

data_verbrauch_max = data['Verbrauch'].max()

date_consumption_max = data['Datum'][data['Verbrauch'] == data_verbrauch_max]
print(date_consumption_max.to_string(index=False))
#date_consumption_max = data[1][data[2] == data_verbrauch_max]
#date_test = dt.date(date_consumption_max)
#print(date_test)
#the_time_3 = dt.strptime(date_consumption_max, '%m')
#month = date_consumption_max.month
#print(month)
dates = np.array(date_consumption_max)
check1 = panda.to_datetime(dates).month
#summer = np.timedelta64(5,'M')
#print(summer)

if check1 > 5 and check1 < 10:
    print("Yuhu, Summer!!")
    print(date_consumption_max['Datum','Verbrauch'])
else:
    print("Oops, pipe bursted!!")
    print(date_consumption_max)


#data["Datum"] = data[date_consumption_max].dt.month

#print(var)

#test

#print(data_verbrauch_max)
#print(panda.to_datetime(dates).month)
#print(date_consumption_max.month)
#print (data['Datum'][data['Verbrauch'] == data_verbrauch_max])
"""
