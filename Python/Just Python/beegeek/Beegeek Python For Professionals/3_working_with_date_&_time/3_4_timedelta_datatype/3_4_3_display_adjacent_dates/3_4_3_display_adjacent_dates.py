'''
TODO:   
        Write a program that takes a date as input and outputs the previous and next dates.

NOTE:   
        It is guaranteed that the submitted date has a previous and a next date.        
'''
from datetime import datetime, timedelta


DATE_FORMAT = '%d.%m.%Y'

def get_user_date():
    return datetime.strptime(input('Please input date in format DD.MM.YYYY: '), DATE_FORMAT)

def display_adjacent_dates(current_date):
    current_timedelta = timedelta(days=1)
    
    previous_date = current_date - current_timedelta
    next_date = current_date + current_timedelta

    print(previous_date.strftime(DATE_FORMAT), next_date.strftime(DATE_FORMAT), sep='\n')


giving_date = get_user_date()
display_adjacent_dates(giving_date)