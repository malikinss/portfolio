'''
TODO:   
        Implement a function num_of_sundays() that takes one argument as input:
            year — natural number, year
        
        The function should return the number of Sundays in the year year.
 
'''
from datetime import datetime, timedelta

def get_next_weekday_date(current_date, target_weekday):
    weekday_of_current_date = current_date.weekday()
    days_to_next_weekday = (target_weekday - weekday_of_current_date) % 7

    next_weekday_date = current_date + timedelta(days=days_to_next_weekday)
    
    return next_weekday_date

def calculate_num_of_sundays(first_sunday, last_sunday):
    difference_days = (last_sunday - first_sunday).days

    num_of_sundays = difference_days // 7  # Consider only full weeks

    if last_sunday.year == first_sunday.year:
        num_of_sundays += 1

    return num_of_sundays

def num_of_sundays(year):
    sunday = 6
    first_day_of_year = datetime(year, 1, 1)
    last_day_of_year = datetime(year, 12, 31)

    first_sunday = get_next_weekday_date(first_day_of_year, sunday)
    last_sunday = get_next_weekday_date(last_day_of_year, sunday)
    
    num_of_sundays = calculate_num_of_sundays(first_sunday, last_sunday)

    return num_of_sundays

print(num_of_sundays(2024))