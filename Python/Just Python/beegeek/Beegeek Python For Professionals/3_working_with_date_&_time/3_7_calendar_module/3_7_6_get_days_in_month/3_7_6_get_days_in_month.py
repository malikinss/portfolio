'''
TODO:   
        Implement a function get_days_in_month() that takes two arguments in the following order:
            year — natural number
            month — full name of the month in English

        The function should return a list, sorted in ascending order, of all dates (type date) of the month month and year year.    
'''
import calendar
from datetime import datetime

DATE_FORMAT = '%Y-%m-%d'
ENG_MONTH_NAMES = list(calendar.month_name)

def parse_date(date_string):
    try:
        return datetime.strptime(date_string, DATE_FORMAT).date()
    except ValueError:
        raise ValueError('Invalid datetime format. Please use the format DD.MM.YYYY HH:MM')  

def get_number_of_month_by_name(month_name):
    return ENG_MONTH_NAMES.index(month_name)

def get_number_of_days_in_month(year, month):
    _, number_of_days = calendar.monthrange(year, month)

    return number_of_days

def get_days_in_month(year, month):
    month_num = get_number_of_month_by_name(month)
    days_number = get_number_of_days_in_month(year, month_num)

    result_list = []

    for day_num in range(1, days_number+1):
        combined_date = f"{year}-{month_num:02d}-{day_num:02d}"
        cur_date = parse_date(combined_date)
        result_list.append(cur_date)

    return result_list    

get_days_in_month(2021, 'December')