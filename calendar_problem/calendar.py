import sys
from typing import Dict


# Week start from 1901-01-01
WEEKSTART: Dict[str, int] = {
    "monday" : 7,
    "tuesday" : 1,
    "wednesday" : 2,
    "thursday" : 3,
    "friday" : 4,
    "saturday" : 5,
    "sunday" : 6,
}

# month_endday
month_endday: Dict[str, int] = {
    '1' : 31,
    '2' : 28, # if leap year, value will be change(default is 28)
    '3' : 31,
    '4' : 30,
    '5' : 31,
    '6' : 30,
    '7' : 31,
    '8' : 31,
    '9' : 30,
    '10' : 31,
    '11' : 30,
    '12' : 31,
}

def leap_year_check(year: int = 0) -> bool:
    """### Check for leap year

    Args:
        year (int): int type year data
    Returns:
        bool: True if leap year
    """
    feb_end: int = 0 # default
    
    if bool(year) is True and year > 1900:
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    feb_end = 29
                else:
                    feb_end = 28
            else:
                feb_end = 29
        else:
            feb_end = 28
            
        month_endday['2'] = feb_end
    else:
        print("Please Input Correct Data -> ex: 2000")
        
    if feb_end == 29:
        return True
    else:
        return False
    
def count_first_day_of_month(start_year: int, end_year: int, weekday: str, echo: bool = False) -> int:
    """### Count method for day of the month from year\n
    * This function only work that start year's jan 1 to end year's dec 31
    * Count for 1st of The Month

    Args:
        start_year (int): start of year number -> 1901
        end_year (int): end of year number -> 2000
        weekday (str): Want to count for the first day of the month -> monday
        echo (bool): print working process on terminal
    """
    month: int = 1 # it will be reset when year is changed
    day: int = WEEKSTART[weekday] # it will be reset when month is changed
    year: int = start_year # it will be +1 when year is changed
    count: int = 0 # count of specific days
    
    # check arg logic
    if weekday not in WEEKSTART and bool(weekday) is False: 
        print("Please Input Correct Data -> ex: if you want input january type 'jan'")
        sys.exit()
    else:
        pass
    if start_year < 1901 and end_year > 1901:
        print("Please Input Correct Data -> start year: 1901~, end year: 1902~ ")
        sys.exit()
    else:
        pass
    
    # calculate logic
    while True:
        if year > end_year:
            break
        else:
            leap_year = leap_year_check(year)
            if echo is True: print(f'\n{year} - {leap_year}')
            while True:
                if day == 1:
                    if echo is True: print(f"{month}/{day}")
                    count += 1
                day += 7
                if day > month_endday[str(month)]:
                    day = day - month_endday[str(month)]
                    month += 1
                    if month > 12:
                        month = 1
                        year += 1
                        break
    return count
    
if __name__ == "__main__":
    count_first_day_of_month(1901, 2000, "sunday", True)