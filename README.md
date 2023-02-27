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
Also the user is been asked to give the length, the width and the volume of the water tank.

## Plausibility check
The plausibility check valuates, of the days with the maximum consumption are realistic. From engineering experience, the day with the highest consumption have to be in the summer time due to higher water consumption in this period. The plausibility check evaluates for every given year, if the day with the highest outflow is in summer or winter. If it is in summer, the value gets deleted. After that the code saves the new data in a new .xlcx file, so it can be imported again.


## Calculating the 3 categories
The plausibility check valuates, of the days with the maximum consumption are realistic. From engineering experience, the day with the highest consumption have to be in the summer time due to higher water consumption in this period. The plausibility check evaluates for every given year, if the day with the highest outflow is in summer or winter. If it is in summer, the value gets deleted. After that the code saves the new data in a new .xlcx file, so it can be imported again.


## Final Calculation
In the final calculation the codes first compares the highest tank volume demand of the three categories and takes the biggest one. After that, the biggest demanded volume is compared to the given volume of the real water tank. The user gets a message if the water tank volume is big enough.
