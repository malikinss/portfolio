'''
TODO:   
        Implement a function fill_up_missing_dates() that takes one argument as input:
            dates — list of string dates in DD.MM.YYYY format

        The function should return a list containing all the dates in the dates list, in ascending order, plus any missing dates in between.

NOTE:
        Let's look at the first test. The dates list contains the period from 01.11.2021 to 07.11.2021
            dates = ['01.11.2021', '07.11.2021', '04.11.2021', '03.11.2021']
        missing dates 02.11.2021, 05.11.2021, 06.11.2021.
        Then the function call:
            fill_up_missing_dates(dates)
        should return a list:
            ['01.11.2021', '02.11.2021', '03.11.2021', '04.11.2021', '05.11.2021', '06.11.2021', '07.11.2021']

        The function should create and return a new list, and not modify the passed one.

'''
from datetime import datetime, timedelta

DATE_FORMAT = '%d.%m.%Y'

def convert_to_datetime(string_date):
    try:
        return datetime.strptime(string_date, DATE_FORMAT)
    except ValueError:
        raise ValueError('Invalid date format. Please use the format DD.MM.YYYY')

def get_datetime_sorted_dates(string_dates):
    return sorted([convert_to_datetime(date) for date in string_dates])

def get_string_dates(datetime_dates): 
    return [date.strftime(DATE_FORMAT) for date in datetime_dates] 

def get_dates_range(start_date, end_date):
    dates = []
    current_date = start_date

    while current_date <= end_date:
        dates.append(current_date)
        current_date += timedelta(days=1)

    return dates

def fill_up_missing_dates(dates):
    # Convert string dates to datetime objects and sort them
    dates_dt = sorted([convert_to_datetime(date) for date in dates])
    
    min_date = min(dates_dt)
    max_date = max(dates_dt)

    # Get the range of dates between the minimum and maximum dates
    new_dates = get_dates_range(min_date, max_date)

    # Convert the new datetime dates back to strings
    new_dates_string = get_string_dates(new_dates)   

    return new_dates_string

dates = ['01.11.2021', '04.11.2021', '09.11.2021', '15.11.2021']
print(fill_up_missing_dates(dates))