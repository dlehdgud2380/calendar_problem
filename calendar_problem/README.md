# calendar_problem
## Stack
* Python3
* Dict
## Logic Info
* Leap Year calculate logic.
* Calculate specific weekday for first of the month from start of year and end of year.
* You can see process working from echo enable
## Getting Started
### excute
1. python3 calendar.py
### change value and excute
1. open calendar.py using text editor
2. change count_first_day_of_month()'s arg
```
example:

count_first_day_of_month(1901, 2000, "sunday")
count_first_day_of_month(1950, 2000, "saturday")
```
3. python3 calendar.py
## caution
### count_first_day_of_month()
```
count_first_day_of_month(start_year: int, end_year: int, weekday: str, echo: bool)
```
* start_year > 1900
* end_year > 1902
* weekday: "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"
* echo: True, False
### leap_year_check()
```
def leap_year_check(year: int)
```
* year > 1900, default is 0
