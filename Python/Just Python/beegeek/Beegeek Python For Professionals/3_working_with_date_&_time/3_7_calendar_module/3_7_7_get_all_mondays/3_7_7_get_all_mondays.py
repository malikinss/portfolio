'''
TODO:   
        Implement a function get_all_mondays() that takes one argument:
            year — natural number
        
        The function should return a list, sorted in ascending order, of all dates (type date) in the year year that fall on Monday. 
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

def get_all_mondays(year):
    mondays = []

    for month_name in ENG_MONTH_NAMES:
        if month_name == '':
            continue

        mondays_in_cur_month =  filter_dates_by_weekday_in_month(year, month_name, 0)

        mondays.extend(mondays_in_cur_month)

    return mondays    

mondays = get_all_mondays(111)
print(*mondays, sep='\n')