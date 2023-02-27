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
Here a class `Plausbility` is defined, where two arguments *data* and *year* are defined.
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
For calculating the three categories *pandas* will be needed again. 
Here in `category.py` the class `Tank` is defined. In the `__init__`the variables used in this class are called.
```python
class Tank:
    def __init__(self):
        self.length = 0
        self.width = 0
        self.floor_area = 0
        self.volume = 0
        self.qdmax = 0
        self.criteria_1 = 0
        self.criteria_2 = 0
        self.criteria_3 = 0
```
These variables are given the value 0 for now. In the following they will be defined through inputs.

First the measurements of the tank are needed from the user.
Therefore the function `tank_data` is defined.
```python
def tank_data(self):
    print("\nFirst you need to name the size of your tank.")
```
The length will be defined through an input of the user. This is achieved through `length = int(input())`
If the input is 0 or less than 0 an error message will be given as the length of the tank can not be 0 or even negative.
```python
while True:
    try:
        self.length = int(input("Please insert the length of the tank in meter. "))
    except ValueError:
        print("Wrong input.")
        logging.exception("The input for the tank length is wrong.")
        continue
    else:
        break

while self.length <= 0:
    print("Wrong input, the length can not be 0 or less.")
    logging.error("User input for length <= 0.")
    while True:
        try:
            self.length = int(input("Please insert the length of the tank in meter. "))
        except ValueError:
            print("Wrong input.")
            logging.exception("The input for the tank length is wrong.")
            continue
        else:
            break
```

The same thing will be done for the width using `width = int(input())`.
here there will come an error too if the input is 0 or negative.
```python
while True:
    try:
        self.width = int(input("Please insert the width of the tank in meter. "))
    except ValueError:
        print("Wrong input.")
        logging.exception("The input for the tank width is wrong.")
        continue
    else:
        break

while self.width <= 0:
    print("Wrong input, the width can not be 0 or less.")
    logging.error("User input for width <= 0.")
    while True:
        try:
            self.width = int(input("Please insert the width of the tank in meter. "))
        except ValueError:
            print("Wrong input.")
            logging.exception("The input for the tank width is wrong.")
            continue
        else:
            break
```
As for the categories the floor area is needed, it is being calculated by multiplying the length and width input.
```python
self.floor_area = self.width * self.length
        logging.info(f"The calculated area for the tank is {self.floor_area} m^2.")
```
One last measurement of the tank that is needed is the volume of tank for the final comparison of the calculated volume with the actual volume.
Therefore using `int(input())` the volume is asked for.
```python
while True:
    try:
        self.volume = int(input("Please insert the volume of the tank in cubic meter. "))
    except ValueError:
        print("Wrong input.")
        logging.exception("The input for the tank volume is wrong.")
        continue
    else:
        break

while self.volume <= 0:
    print("Wrong input, the volume can not be 0 or less.")
    logging.error("User input for volume <= 0.")
    while True:
        try:
            self.volume = int(input("Please insert the volume of the tank in cubic meter. "))
        except ValueError:
            print("Wrong input.")
            logging.exception("The input for the tank volume is wrong.")
            continue
        else:
            break
```

Now each category will be calculated.
1. Category 1

As the raw data was already checked through the plausibility check we need to import the plausible data. Using *pandas* the data is imported.
```python
def category_1(self):
    data_2017 = pd.read_excel(r'data\\Plausible_Consumption_2017.xlsx')
    data_2018 = pd.read_excel(r'data\\Plausible_Consumption_2018.xlsx')
    data_2019 = pd.read_excel(r'data\\Plausible_Consumption_2019.xlsx')
```
This will be put into a list
```python
data = list()
    data.append(data_2017)
    data.append(data_2018)
    data.append(data_2019)
```
Now the maximum consumption of the plausible data are being determined using `data.max()` 
```python
data_2017_df_cons_max = data_2017['Consumption'].max()
    data_2018_df_cons_max = data_2018['Consumption'].max()
    data_2019_df_cons_max = data_2019['Consumption'].max()
```
These maximum consumption of the years are being put into a list using `list()`
```python
my_data = list()
    my_data.append(data_2017_df_cons_max)
    my_data.append(data_2018_df_cons_max)
    my_data.append(data_2019_df_cons_max)
```
As for the first criteria the highest daily consumption is needed. Now the highest daily consumption of the past years can be determined with `max()`.
Then the volume of the first criteria can be calculated with multiplying the highest daily consumption with `0.5`.
```python
self.qdmax = max(my_data)
self.criteria_1 = 0.5 * self.qdmax
print(f"Criteria 1 = {self.criteria_1} m^3")
```
2. Category 2

For the second criteria the water volume in case of fire needs to be calculated.
Here several informations are needed to determine the fire volume. 
The informations needed are given as a choice for the user to choose.
If the user is giving something not given as an option an error message will be given.

First it will be asked in what category the area is grouped as a residence, commercial and industrial are have a different water volume for fire fighting.
```python
def category_2(self):
        # the while True checks, if the input is correct
    area = 0
    print('Is the supplied area a residence (1), a commercial (2) or a industrial (3) area?')
    while True:
        try:
            area = int(input("Please insert 1 for residence, 2 for commercial and 3 for industrial area: "))
        except ValueError:
            print("Wrong input, that is not one of the given options.")
            logging.exception("User input for area is not a number.")
            continue
        else:
            break
```
If the input is not one of the options **(1,2,3)** then these error messages will be given.
```python
while area == 0:
    print("Wrong input, that is not one of the given options.")
    logging.error("User input for area == 0.")
    while True:
        try:
            area = int(input("Please insert 1 for residence, 2 for commercial and 3 for industrial area: "))
        except ValueError:
            print("Wrong input, that is not one of the given options.")
            logging.exception("User input for area is not a number.")
            continue
        else:
            break

while area >= 4:
    print("Wrong input, that is not one of the given options.")
    logging.error("User input for area >= 4.")
    while True:
        try:
            area = int(input("Please insert 1 for residence, 2 for commercial and 3 for industrial area: "))
        except ValueError:
            print("Wrong input, that is not one of the given options.")
            logging.exception("User input for area is not a number.")
            continue
        else:
            break
```
If the input is correct and the first option is selected **residence (1)** there is another information needed.
The number of stories of the highest building in the area is needed. Therefore another `int(input())` is needed.
```python
if area == 1:
    print("What is the maximum number of floors in the area? ")
    while True:
        try:
            floors_number = int(input("Please insert a number: "))
        except ValueError:
            print("Wrong input!")
            logging.exception("User input for floor is not a number.")
            continue
        else:
            break
```
Here as well an error message will come if the input is wrong.
```python
while floors_number == 0:
    print("Wrong input, if the floor number is '0', there would be no building.")
    logging.error("User input for floor number == 0.")
    while True:
        try:
            floors_number = int(input("Please insert a number: "))
        except ValueError:
            print("Wrong input!")
            logging.exception("User input for floor number is not a number.")
            continue
        else:
            break
```
With an *if* statement now all the scenarios are being gone through.
In each scenario one more input is needed. THe spread risk of the fire should be either **small**, **medium** or **high**.

First if the number of stories are less than **3** the fire volume depending of the spread risk will be either **48 m³** or **96 m³**.
```python
if floors_number <= 3:
    logging.info(f"The user input for floors number is {floors_number}.")
                # Getting the risks of a fire spread
    spread_risk = input("Is the risk of fire spread in the area small, medium or high?"
                        "\nIf you do not know, ask the responsible fire department. ")

                # The while funktion checks, if the input is correct.
    while spread_risk != "small" and spread_risk != "medium" and spread_risk != "high":
        spread_risk = input("This is neither 'small', 'medium', or 'high'."
                            "\nPlease check the risk of fire spread and insert on of the three terms. ")
        logging.error("The input for the fire risk is neither small, medium or high.")

    if spread_risk == "small":
        v_fire = 2 * 48
    if spread_risk == "medium":
        v_fire = 2 * 96
    if spread_risk == "high":
        v_fire = 2 * 96
```
If the stories are higher than **3** then the fire volume will be either **96 m³** or **192 m³**.
```python
else:
    logging.info(f"The user input for floors number is {floors_number}.")
    spread_risk = input("Is the risk of fire spread in the area small, medium or high?"
                        "\nIf you do not know, ask the responsible fire department. ")

    while spread_risk != "small" and spread_risk != "medium" and spread_risk != "high":
        spread_risk = input("This is neither 'small', 'medium', or 'high'."
                            "\nPlease check the risk of fire spread and insert on of the three terms. ")
        logging.error("The input for the fire risk is neither small, medium or high.")

    if spread_risk == "small":
        v_fire = 2 * 96
    if spread_risk == "medium":
        v_fire = 2 * 96
    if spread_risk == "high":
        v_fire = 2 * 192
```
For the 

3. Category 3
## Evaluating the current volume
