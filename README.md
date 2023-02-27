### Python Programming for Water Resources Engineering and Research

## Final Student Project: Automation of DVGW W300-1 compliant tank design

![flood](https://www.stuttgart.de/leben/umwelt/wasser/trinkwasser.php.media/274485/ausschnitt-hochbehaelter.jpg.scaled/932464ec1764f8644c24b343c4cd7baf.jpg)
Source: https://www.stuttgart.de/leben/umwelt/wasser/trinkwasser.php

>   ***Goals***: This package will determine if an existing water tank in a drinking water system has a compatible volume for the current water demand.
> If not, a suitable volume will be given.

>   ***Requirements***: Python libraries: numpy, pandas and matplotlib 

## Terminology
As the demand of an area can change with time the needed volume of a water 
tank supplying this area may also change. Therefore, using past daily consumption 
data of the last couple of years as well as the hourly inflow and outflow of the 
water tank on a peak day a new needed volume should be determined.

## Data Import
Using *pandas* the daily consumption of the area will be imported. In `main.py` the latest daily consumption of the past years are being imported with `pd.read_excel`.
```python
import panda as pd
data_2017 = pd.read_excel(r'data\\Consumption_2017.xlsx')
data_2018 = pd.read_excel(r'data\\Consumption_2018.xlsx')
data_2019 = pd.read_excel(r'data\\Consumption_2019.xlsx')
```

## Plausibility check
In `plausibility.py` the plausibility of the data will be checked. 
Here a class is defined, where two arguments *data* and *year* are defined.
Here the libraries *pandas* and *numpy* are needed.
```python
import pandas as pd
import numpy as np
class Plausibility:
    def __init__(self, data, year):
        self.data = data
        self.year = year
```
The *data* should later be selected from the imported data. Whereas the year is defined as a string.

A second function will be defined as `check_plausibility`.
```python
def check_plausibility(self):
    i = 1
    while i > 0:
            # get the maximum consumption
        data_cons_max = self.data['Consumption'].max()
            # get the date of the maximum consumption
        date_cons_max = self.data['Date'][self.data['Consumption'] == data_cons_max]
            # get the month of the date of the maximum consumption
        date_peak_day = np.array(date_cons_max)
        month_peak_day = pd.to_datetime(date_peak_day).month
```
Here we use the *while* statement to see if the month of the daily peak consumption is a "Summer" month. 
The *while* loop will continue until the month is a "Summer" month (`i = 0`).
The steps that are being done here is first getting the highest daily consumption using `data.max()`
After that the date where the highest daily consumption occurred is taken with `data[][data[] == data.max()]`
To be able to determine the month we need to use `np.array()` and `pd.to_datetime().month`.

After getting the month we will use the *if* statement to see if the month is a "Summer" month.
Here we defined Summer from June to September.
```python
if 5 < month_peak_day < 10:
    i = 0
                # the plausible data will be exported into an Excel file
    self.data.to_excel("data\\Plausible_Consumption_" + self.year + ".xlsx", index=False)
    logging.info(f"The user input for {self.year} is yes.")
else:
    i = 1
            # get the index where the daily consumption is maximum
    index = np.argmax(self.data['Consumption'])
    logging.info(f"The raw {index} was a wrong value and was extinguished.")
                # delete the row where the maximum daily consumption is located
    self.data = self.data.drop(index)
```
Here we say check with the *if* statement if the month is between Mai and October with `5 < month_peak_day < 10`.
- If it is between those months then the variable *i* will get the value 1. So, the *while* loop can close. 
  As here the daily peak consumption is already or finally in summer the data will be saved into an Excel `.xlsx` file in the *data* folder.
- If it is not between those months we will delete that consumption. Therefore the row (index) of the maximum daily consumption will be determined with `np.argmax()`.
  Afer getting the index the row with the maximum daily consumption will be deleted using `data.drop()`.


## Calculating the 3 categories
For calculating the 

## Evaluating the current volume
