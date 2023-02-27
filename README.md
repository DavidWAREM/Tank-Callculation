### Python Programming for Water Resources Engineering and Research

## Final Student Project: Automation of DVGW W300-1 compliant tank design

![flood](https://www.stuttgart.de/leben/umwelt/wasser/trinkwasser.php.media/274485/ausschnitt-hochbehaelter.jpg.scaled/932464ec1764f8644c24b343c4cd7baf.jpg)

>   ***Goals***: This package will determine if an existing water tank in a drinking water system has a compatible volume for the current water demand.
> If not, a suitable volume will be given.

>   ***Requirements***: Python libraries: pandas and matplotlib 

## Terminology
As the demand of an area can change with time the needed volume of a water 
tank supplying this area may also change. Therefore, using past daily consumption 
data of the last couple of years as well as the hourly inflow and outflow of the 
water tank on a peak day a new needed volume should be determined.

## Data Import
Using *pandas* the daily consumption of the area will be imported. 
In the Pyhton file `main.py` all the daily consumption data will be imported.

```python
import pandas as pd
data_2014 = pd.read_excel(r'data\\Consumption_2014.xlsx')
data_2015 = pd.read_excel(r'data\\Consumption_2015.xlsx')
data_2016 = pd.read_excel(r'data\\Consumption_2016.xlsx')
data_2017 = pd.read_excel(r'data\\Consumption_2017.xlsx')
data_2018 = pd.read_excel(r'data\\Consumption_2018.xlsx')
data_2019 = pd.read_excel(r'data\\Consumption_2019.xlsx')
```

## Plausibility check
Before the data can be used for the determination of the daily peak consumption (Qdmax) the data has to be checked for the plausibility.

First we can try and look if the data could be not plausible. With calling the `plot_data` from `plotdata.py` the data will be plotted if the user wants it.
```python
from plotdata import plot_data
plot_in = input("Should the Consumption in "+year+" be shown? (Please answer in yes/no)")
        if plot_in == "yes":
            plot_data(data['Date'], data['Consumption'], "Daily Consumption", "Date [year-month]", "Consumption[M3/day]",
                    10, "navy",True)
            logging.info(f"The user input for {year} is yes.")
        elif plot_in == "no":
            plot_data(data['Date'], data['Consumption'], "Daily Consumption", "Date [year-month]", "Consumption[M3/day]",
                    10,"navy", False)
            logging.info(f"The user input for {year} =! yes.")
```

Afterwards the data will be checked for the plausibility using a `while` statement. 
First we determine `i = 1` and we loop the steps  `while i > 0`.
- The function will get the maximum consumption from the selected data with `data['Consumption'].max()`
- With the determined maximum consumption the date of that consumption can be taken through `data['Date'][data['Consumption'] == data_cons_max]`
- Now the month of that date needs to be taken out. Here we need to save the date into an array using `np.array` and then taking the month using `pd.to_datetime(date_peak_day).month`
```python
i = 1
    while i > 0 :
        data_cons_max = data['Consumption'].max()
        date_cons_max = data['Date'][data['Consumption'] == data_cons_max]
        date_peak_day = np.array(date_cons_max)
        month_peak_day = pd.to_datetime(date_peak_day).month
```
Inside the `while` loop we now put an `if`statement to see if the month of the date with maximum consumption is a "Summer"-month.
- If the month is a "Summer"-month then `if month_peak_day > 5 and month_peak_day < 10`. Here we determine that Summer is starting in June and ending in September.
    As it is a "Summer"-month we can set the `i = 0`. So, the while loop will finish/close. And the data will be saved as a `.xlsx`file in the data folder.
- If the month is not in "Summer" the `i` will stay `1`and the row of that date will be deleted. This is achieved using `np.argmax`and `data.drop()`.
```python
if month_peak_day > 5 and month_peak_day < 10:
    i = 0
    data.to_excel("data\Plausible_Consumption_"+year+".xlsx", index=False)
    logging.info(f"The user input for {year} is yes.")
else:
    i = 1
    index = np.argmax(data['Consumption'])
    logging.info(f"The raw {index} was a wrong value and was extinguished.")
    data = data.drop(index)
```
After the `while` loop is finished a statement will be given that the plausibility check has been done and the Qdmax and the date will be shown.
```python
print("Plausibility check for the consumption in " + year + " successfully ran. The Qdmax is = " +
            str(data_cons_max) + " m^3/d (" + date_cons_max.to_string(index=False) + ")")
```
## Calculating the 3 categories
In the `category.py` file is the class `Tank` defined. In this class all the categories will be calculated.
```python
def __init__(self):
    """Initialise attributes."""
    self.length = 0
    self.width = 0
    self.floor_area = 0
    self.volume = 0
    self.qdmax = 0
    self.criteria_1 = 0
    self.criteria_2 = 0
    self.criteria_3 = 0
```
First the measurements of the tank are needed. Therefore here with `int(input())`the values for the length can be given by the user.
```python
def tank_data(self):
    print("\nFirst you need to name the size of your tank.")while True:
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
Same in this step with `int(input())` the width of the tank can be given.
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
THe next step will be calculating the floor area of the tank. This is given by multiplying the input of the length and width of the tank.
```python
self.floor_area = self.width * self.length
        logging.info(f"The calculated area for the tank is {self.floor_area} m^2.")
```
Another measurement of the tank is the tank volume. Therefore another input of the user needs to be done. Same with the `(int(input())` the volume can be written here.
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

1. Category 1

For the first category the highest Qdmax of the last years is needed.
As we already did a plausibility check of the raw data. Now we need to import the plausible data. With `pd.read_excel()` we can import the plausible data that was created before.
```python
data_2014 = pd.read_excel(r'data\\Plausible_Consumption_2014.xlsx')
data_2015 = pd.read_excel(r'data\\Plausible_Consumption_2015.xlsx')
data_2016 = pd.read_excel(r'data\\Plausible_Consumption_2016.xlsx')
data_2017 = pd.read_excel(r'data\\Plausible_Consumption_2017.xlsx')
data_2018 = pd.read_excel(r'data\\Plausible_Consumption_2018.xlsx')
data_2019 = pd.read_excel(r'data\\Plausible_Consumption_2019.xlsx')
```
```python
data = list()
    data.append(data_2014)
    data.append(data_2015)
    data.append(data_2016)
    data.append(data_2017)
    data.append(data_2018)
    data.append(data_2019)
```
```python
data_2014_df_cons_max = data_2014['Consumption'].max()
    data_2015_df_cons_max = data_2015['Consumption'].max()
    data_2016_df_cons_max = data_2016['Consumption'].max()
    data_2017_df_cons_max = data_2017['Consumption'].max()
    data_2018_df_cons_max = data_2018['Consumption'].max()
    data_2019_df_cons_max = data_2019['Consumption'].max()
```
```python
my_data = list()
    my_data.append(data_2014_df_cons_max)
    my_data.append(data_2015_df_cons_max)
    my_data.append(data_2016_df_cons_max)
    my_data.append(data_2017_df_cons_max)
    my_data.append(data_2018_df_cons_max)
    my_data.append(data_2019_df_cons_max)
```
```python
self.qdmax = max(my_data)
        logging.info(f"The max. amount of outflow is {self.qdmax}.")
```
```python
self.criteria_1 = 0.5 * self.qdmax
    print(f"Criteria 1 = {self.criteria_1} m^3")
    logging.info(f"The category 1 is {self.criteria_1}.")
```
2. Category 2
```python
def category_2(self):
    area = 0
    print('Is the supplied area a residual (1), a commercial (2) or a industrial (3) area?')
    while True:
        try:
            area = int(input("Please insert 1 for residual, 2 for commercial and 3 for industrial area: "))
        except ValueError:
            print("Wrong input, that is not one of the given options.")
            logging.exception("User input for area is not a number.")
            continue
        else:
            break
```
```python
while area == 0:
    print("Wrong input, that is not one of the given options.")
    logging.error("User input for area == 0.")
    while True:
        try:
            area = int(input("Please insert 1 for residual, 2 for commercial and 3 for industrial area: "))
        except ValueError:
            print("Wrong input, that is not one of the given options.")
            logging.exception("User input for area is not a number.")
            continue
        else:
            break
```
```python
while area >= 4:
    print("Wrong input, that is not one of the given options.")
    logging.error("User input for area >= 4.")
    while True:
        try:
            area = int(input("Please insert 1 for residual, 2 for commercial and 3 for industrial area: "))
        except ValueError:
            print("Wrong input, that is not one of the given options.")
            logging.exception("User input for area is not a number.")
            continue
        else:
            break
```
```python
if area == 1:
    # If the area is a Residual, this is the branch.
    # The while True checks, is the input for the floor number is correct.
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
```python
if area == 2:
    # Again the while True checks, if the input is correct.
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

    # Checks if the floor number is not '0'.
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
```python
# If it is an industrial area, this is the branch.
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

logging.info(f"The user input for the area is a {area}.")
logging.info(f"The user input for the risk of a fire spread is {spread_risk}.")

"""The Category 2 is calculated by the amount for the firefighter plus qdmax * 0.3."""
self.criteria_2 = v_fire + 0.3 * self.qdmax
print(f"Criteria 2 = {self.criteria_2} m^3.")
```


3. Category 3
```python
def category_3(self):

    # Here the hourly inflow and outflow data will be imported to python.
    df_outflow_2018 = pd.read_excel('data\\Verbrauch_2018_hourly.xlsx')
    df_outflow_2019 = pd.read_excel('data\\Verbrauch_2019_hourly.xlsx')
    logging.info("The hourly outflow data are properly loaded into the system.")

    df_inflow_2018 = pd.read_excel('data\\Inflow_2018_hourly.xlsx')
    df_inflow_2019 = pd.read_excel('data\\Inflow_2019_hourly.xlsx')
    logging.info("The hourly inflow data are properly loaded into the system.")
```
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
```python
def final_calculation(self):
    criteria = {"Category 1, qdmax": self.criteria_1,
                "Category 2, additional water for firefighters": self.criteria_2,
                "Criteria 3, volume needed to maintain a minimum water level in the water tank": self.criteria_3}
    criteria_max = max(self.criteria_1, self.criteria_2, self.criteria_3)
    if criteria_max <= self.volume:
        print("The given tank is big enough for the given situation."
                f"\nThe minimum tank volume would be {criteria_max} m^3 from {max(criteria)}.")
        logging.info("The given tank is big enough.")
    else:
        print("The given tank is not big enough for the given situation."
                f"\nThe given volume was {self.volume} m^3.")
        print(f"The needed volume regarding this situation would be {criteria_max} m^3 from {max(criteria)}.")
        logging.info("The given tank is not big enough for the given situation.")
        logging.info(f"The needed volume regarding this situation would be {criteria_max} m^3 from {max(criteria)}.")
```
