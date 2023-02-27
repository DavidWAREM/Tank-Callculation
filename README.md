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

Based on the DVGW W300-1 the tank should cover up certain scenarios. Therefore the following categories are defined:
1. The Volume should at least be able to supply the area for half a day of a day with maximum consumption:
    **V = 0.5 * Qdmax**
2. In case of a fire the tank should be able to give water for fire fighting for 2 hours while being able to cover about one third of a day (~ 7 hours) of a day with maximum consumption: 
    **V = (2 * V_fire) + (0.3 * Qdmax)**
3. As the tank should not be empty as otherwise air could enter the pipes the tank should always hava a minimum volume inside. Therefore a minimum water height of 0.5 m is needed in the tank
   The tank is also needed to equalize the fluctuation of the water consumption in the area.
   Adding both volumes the needed volume: **V = Q_fluk + Q_min**

As the tank should cover all scenarios, only the biggest volume needs to be compared with the current volume of the water tank. 
So, we can determine if the tank is big enough or even too big so the volume needs to be reduced or if it is to small and needs to be planned new with a bigger volume.

## Run the programm
As all the classes and functions are already called in the `main.py` the `main.py`can be directly run and it will give the final result.
```python
import pandas as pd
from plausibility import Plausibility, PlotDaily
from fun import *
from category import Tank

print("This algorithm will calculate, if the given tank is big enough for the given outflow data,"
      "\nregarding the German law for water supply facilities.")

if __name__ == '__main__':
    start_logging()

    p_2017 = Plausibility(data_raw_2017, "2017")
    pl_2017 = PlotDaily(data_raw_2017, "2017")
    p_2018 = Plausibility(data_raw_2018, "2018")
    pl_2018 = PlotDaily(data_raw_2018, "2018")
    p_2019 = Plausibility(data_raw_2019, "2019")
    pl_2019 = PlotDaily(data_raw_2019, "2019")
    pl_2017.plot_daily()
    p_2017.check_plausibility()
    pl_2018.plot_daily()
    p_2018.check_plausibility()
    pl_2019.plot_daily()
    p_2019.check_plausibility()

    my_tank = Tank()
    my_tank.tank_data()
    my_tank.category_1()
    my_tank.category_2()
    my_tank.category_3()
    my_tank.final_calculation()
```
The data import that is also int the `main.py` is explained in the following.

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

        data_cons_max = self.data['Consumption'].max()
        date_cons_max = self.data['Date'][self.data['Consumption'] == data_cons_max]
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
    self.data.to_excel("data\\Plausible_Consumption_" + self.year + ".xlsx", index=False)
    logging.info(f"The user input for {self.year} is yes.")
else:
    i = 1
    index = np.argmax(self.data['Consumption'])
    logging.info(f"The raw {index} was a wrong value and was extinguished.")
    self.data = self.data.drop(index)
```
Here we say check with the *if* statement if the month is between Mai and October with `5 < month_peak_day < 10`.
- If it is between those months then the variable *i* will get the value 1. So, the *while* loop can close. 
  As here the daily peak consumption is already or finally in summer the data will be saved into an Excel `.xlsx` file in the *data* folder.
- If it is not between those months we will delete that consumption. Therefore the row (index) of the maximum daily consumption will be determined with `np.argmax()`.
  Afer getting the index the row with the maximum daily consumption will be deleted using `data.drop()`.

## Ploting Daily consumption
To see the raw data before the data gets checked on plausibility another class in `plausibility.py` is created.
This class inherits from the class `Plausibility` as the arguments can be used again in this class. 
In the function `plot_daily` first the user will be asked if he/she wants to see the plot of the raw data or not.
With this the user can determine to plot the data or not.
```python
class PlotDaily(Plausibility):
    def plot_daily(self):
        plot_in = input("Should the Consumption in " + self.year + " be shown? (Please answer in yes/no)")
```
With the input of the user of **yes** or **no** the `plot_data` function from the `plotdata.py`is calles.
Using the `if` statement the plot will be activated or not.
```python
if plot_in == "yes":
            # plot data
    plot_data(self.data['Date'], self.data['Consumption'], "Daily Consumption", "Date [year-month]",
                "Consumption[M3/day]", 10, "navy", True)
    logging.info(f"The user input for {self.year} is yes.")
elif plot_in == "no":
            # not plotting the data
    plot_data(self.data['Date'], self.data['Consumption'], "Daily Consumption", "Date [year-month]",
                "Consumption[M3/day]", 10, "navy", False)
    logging.info(f"The user input for {self.year} =! yes.")
return True
```
The `plot_data` function is written in the `plotdata.py`
Here besides *pandas*, *numpy* and *matplotlib* are also needed.
With all the needed parameters that are either already determined here or later if the function is called the figura of the plot is created.
```python
def plot_data(date=panda.Series(), consumption=panda.Series(), title="",
            x_label="", y_label="", size=10, color="", ask_plot=True):
    fig, axis = plt.subplots(figsize=(15, 9))
```
With `axis.scatter` a scatter plot is created based on the arguments given.
```python
axis.scatter(x=date, y=consumption,
            marker="o", s=size, color=color)
```
Using `axis.set` the labels of the axes as well as the title of the plot are determined.
With `plot.xlim()` the limit of the x-axis is being determined and with `date.min()` and `date.max()` the limits are set to the minimum and maximum value of the data series of the x-axis.
```python
axis.set(xlabel=x_label, ylabel=y_label, title=title)
plt.xlim(date.min(), date.max())
plt.grid()
```
To give a better look where the maximum daily consumption (Qdmax) is located an arrow will be pointing on it.
With `np.argmax()` the row/index of the maximum consumption can be determined.
So, it can be used in the `axis.annotate` and `arrowprops` to locate where the arrow should point.
```python
index = np.argmax(consumption)
y_max = consumption[index]
x_max = date[index]
axis.annotate('Qdmax', xy=(x_max, y_max), arrowprops=dict(facecolor='red'))
```

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
**1. Category 1**

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
**2. Category 2**

For the second criteria the water volume in case of fire needs to be calculated.
Here several informations are needed to determine the fire volume. 
The informations needed are given as a choice for the user to choose.
If the user is giving something not given as an option an error message will be given.

First it will be asked in what category the area is grouped as a residence, commercial and industrial are have a different water volume for fire fighting.
```python
def category_2(self):
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
    spread_risk = input("Is the risk of fire spread in the area small, medium or high?"
                        "\nIf you do not know, ask the responsible fire department. ")

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
If the first input is **commercial (2)** then the number of stories/floors are also needed.
```python
if area == 2:
    print("What is the maximum number of floors in the area? ")
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
For wrong number of stories another error message will be given.
```python
while floors_number == 0:
    print("Wrong input, if the floor number is '0', there would be no building.")
    logging.error("Input for floor number == 0.")
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
But, using the `if` statement once again, if it has only one storey than the fire volume depending the spread risk again will be either **96 m³** or **192 m³**.
```python
if floors_number <= 1:
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
Otherwise the fire volume will also have **96 m³** or **192 m³**. It differs in the spread risk that the user has to put in.
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
        v_fire = 2 * 192
    if spread_risk == "high":
        v_fire = 2 * 192
```
If the first input is **industrial (3)** the only other input needed to determine the fire volume ist the spread risk.
Here ther fire volume also differs between **96 m³** or **192 m³**.
```python
if area == 3:
    spread_risk = input("Is the risk of fire spread in the area small, medium or high?"
                        "\nIf you do not know, ask the responsible fire department. ")

    while spread_risk != "small" and spread_risk != "medium" and spread_risk != "high":
        spread_risk = input("This is neither 'small', 'medium', or 'high'."
                            "\nPlease check the risk of fire spread and insert on of the three terms. ")
        logging.error("The input for the fire risk is neither small, medium or high.")

    if spread_risk == "small":
        v_fire = 2 * 96
    if spread_risk == "medium":
        v_fire = 2 * 192
    if spread_risk == "high":
        v_fire = 2 * 192
```
After all the inputs have been done by the user, the water volume needed for fire fighting can be determined.
To calculate the volume for **category 2** now the fire volume needs to be added to `0.3 * Qdmax`.
```python
self.criteria_2 = v_fire + 0.3 * self.qdmax
    print(f"Criteria 2 = {self.criteria_2} m^3.")
```

**3. Category 3**
For the last category the hourly inflow and outflow of the water tank are needed.
Therefore using *pandas* again the data will be imported.
```python
df_outflow_2018 = pd.read_excel('data\\Verbrauch_2018_hourly.xlsx')
df_outflow_2019 = pd.read_excel('data\\Verbrauch_2019_hourly.xlsx')
logging.info("The hourly outflow data are properly loaded into the system.")

df_inflow_2018 = pd.read_excel('data\\Inflow_2018_hourly.xlsx')
df_inflow_2019 = pd.read_excel('data\\Inflow_2019_hourly.xlsx')
logging.info("The hourly inflow data are properly loaded into the system.")
```
To get the equalizing volume for the fluctuation in that area the inflow needs to be deducted from the outflow.
This is being done for each row and put into a list using the `for` statement and `list.append()`.
```python
list_df = []
    for index, row in df_inflow_2018.iterrows():
        df_1 = df_inflow_2018.at[index, "inflow"]
        df_2 = df_outflow_2018.at[index, "outflow"]
        df = df_2 - df_1
        list_df.append(df)

    for index, row in df_inflow_2019.iterrows():
        df_1 = df_inflow_2019.at[index, "inflow"]
        df_2 = df_outflow_2019.at[index, "outflow"]
        df = df_2 - df_1
        list_df.append(df)
```
Now the fluctuation volume can be determined by using `max()` from all the fluctuation calculated.
Another important volume is the minimal volume in the tank that is being calculated by multiplying the already calculated *floor area* by **0.5**.
The Volume of the final criteria will be the sum of these two volumes.
```python
q_fluc = max(list_df)
q_min = self.floor_area * 0.5
self.criteria_3 = q_fluc + q_min
logging.info(f"The q_fluc is {q_fluc} m^3.")
logging.info(f"The q_min is {q_min} m^3.")
logging.info(f"The criteria_3 is {self.criteria_3} m^3.")
print(f"The criteria 3 is {self.criteria_3} m^3.")
```

## Evaluating the current volume
For the evaluation of the current tank. In the class `Tank` one more function called `final_calculation` is defined.
Here all the volumes calculated from each category is called and with `max()` the biggest of the volume is selected to be compared with the current volume.
```python
def final_calculation(self):
    criteria = {"Category 1, qdmax": self.criteria_1,
                "Category 2, additional water for firefighters": self.criteria_2,
                "Criteria 3, volume needed to maintain a minimum water level in the water tank": self.criteria_3}
    criteria_max = max(self.criteria_1, self.criteria_2, self.criteria_3)
```
Now with the `if` statement it is being determined if the current tank is big enough or to big for the current consumption.
```python
if criteria_max <= self.volume:
    print("The given tank is big enough for the given situation."
            f"\nThe minimum tank volume would be {criteria_max} m^3 from {max(criteria)}.")
    logging.info("The given tank is big enough.")
else:
    print("The given tank is not big enough for the given situation."
            f"\nThe given volume was {self.volume} m^3.")
    print(f"The needed volume regarding this situation would be {criteria_max} m^3 from {max(criteria)}.")
    logging.info("The given tank is not big enough for the given situation.")
    logging.info(f"The needed volume regarding this situation would be {criteria_max} m^3"
                    f" from {max(criteria)}.")
```
If the current tank is bigger than the volume of the categories then it is big enough or maybe could be smaller.
Whereas if the current volume is smaller than the volume of the categories then the usable volume that the tank needs will be given.