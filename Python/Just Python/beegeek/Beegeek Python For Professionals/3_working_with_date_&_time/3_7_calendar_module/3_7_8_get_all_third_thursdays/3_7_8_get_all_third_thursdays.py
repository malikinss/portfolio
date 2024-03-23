'''
TODO:   
        In many museums, there is one day of the month when visiting the museum for all persons or certain categories of citizens occurs without charging a fee. 
        
        For example, in the Hermitage it is the third Thursday of the month.

        Write a program that determines the dates of free days to visit the Hermitage in a given year.
'''
import calendar
from datetime import datetime

DATE_FORMAT = '%Y-%m-%d'
DATE_FORMAT_2 = '%d.%m.%Y'
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
        combined_date = f"{year:04d}-{month_num:02d}-{day_num:02d}"
        cur_date = parse_date(combined_date)
        result_list.append(cur_date)

    return result_list    

def filter_dates_by_weekday_in_month(year, month, target_weekday):
    result = []
    cur_month_dates = get_days_in_month(year, month)

    for cur_date in cur_month_dates:
        cur_year = cur_date.year
        cur_month = cur_date.month
        cur_day = cur_date.day

        cur_date_weekday = calendar.weekday(cur_year, cur_month, cur_day)

        if cur_date_weekday == target_weekday:
            result.append(cur_date)

    return result        

def get_third_thursday_per_month(year, month_name):
    
    thursdays =  filter_dates_by_weekday_in_month(year, month_name, calendar.THURSDAY)

    return thursdays[2]

def get_all_third_thursdays(year):
    result = []

    for month_name in ENG_MONTH_NAMES:
        if month_name == '':
            continue

        cur_month_third_thursday =  get_third_thursday_per_month(year, month_name)


        result.append(cur_month_third_thursday.strftime(DATE_FORMAT_2))

    return result    

thursdays = get_all_third_thursdays(2021)
print(*thursdays, sep='\n')