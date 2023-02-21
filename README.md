## Python Programming for Water Resources Engineering and Research
# Student Project: Automation of DVGW W300-1 compliant tank design
![Water Tank](https://www.hrgreen.com/wp-content/uploads/2022/03/HRG-Pasadena-water_0855-scaled-1.jpg)
> Image Courtesy
[HR Green - Choosing right water storage community important decision](https://www.hrgreen.com/blog/choosing-right-water-storage-community-important-decision/)

## Background

## Goals

## Requirements

As the demand of an area can change with time the needed volume of a water tank supplying this area may also change. Therefore, using past daily consumption data of the last couple of years as well as the hourly inflow and outflow of the water tank on a peak day a new needed volume should be determined.

## Python Programming
The code is divided into three parts, each one to calculate a criteria. At last, the water tank capacity is the summation of all three criteria. The software library Panda is used to import the excel data and to imported data is handled as a Dataframe, which in-turn uses Numpy.

### Calculate Criteria-1 
| def category_1 | [Category.py](https://github.com/DavidWAREM/Tank-Callculation/blob/74b91ba8ef6bdda234eab08cb95ee560278004be/Category.py#L18) |
| --------- | ----------- |
| Input:    | Data as excel sheets year 2014-2019    |
| Output:   | Criteria-1 = half of maximum discharge |

1. Import Raw Data from Excel Sheets using Pandas' Dataframe, Repeat for years 2014 to 2019
2. The imported Excel Sheets have two Columns: Datum and Verbrauch, find the maximum value from Verbrauch column for each year. 'Datum' column indicates the date and 'Verbauch' column the consumption on this particular date.
3. Create an Array of list with all Maximum water consumption from each year.
4. Calculate maximum discharge in all these years, indicated as 'qdmax'
5. The criteria-1 for capacity calculation shall be half of qdmax.


### Calculate Criteria-2 
| def category_2 | [Category.py](https://github.com/DavidWAREM/Tank-Callculation/blob/74b91ba8ef6bdda234eab08cb95ee560278004be/Category.py#L64) |
| --------- | ----------- |
| Input:    |     |
| Output:   |     |

### Calculate Criteria-3 
| def category_3 | [Category.py](https://github.com/DavidWAREM/Tank-Callculation/blob/74b91ba8ef6bdda234eab08cb95ee560278004be/Category.py#L281) |
| --------- | ----------- |
| Input:    |     |
| Output:   |     |
