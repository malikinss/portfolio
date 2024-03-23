'''
TODO:   
        Write a program that determines the day of the week corresponding to a given date.

        The program input is a date in the YYYY-MM-DD format.

        The program should display the full name of the day of the week in English, which corresponds to the entered date.
'''
import calendar
from datetime import datetime

DATE_FORMAT = '%Y-%m-%d'

def parse_date(date_string):
    try:
        return datetime.strptime(date_string, DATE_FORMAT).date()
    except ValueError:
        raise ValueError('Invalid datetime format. Please use the format DD.MM.YYYY HH:MM')  

def display_weekday(user_date):
    given_date = parse_date(user_date)
    weekdays = list(calendar.day_name)

    weekday_num = calendar.weekday(given_date.year, given_date.month, given_date.day)
    
    print(weekdays[weekday_num])
    
display_weekday(input())