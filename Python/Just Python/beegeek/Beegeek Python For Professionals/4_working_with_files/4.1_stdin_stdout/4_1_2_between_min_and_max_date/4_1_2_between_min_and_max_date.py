'''
TODO:   
        A sequence of dates is given. Write a program that prints the number of days between the maximum and minimum dates of a given sequence.

        An arbitrary number of lines are supplied as input to the program; each line contains a date in ISO format (YYYY-MM-DD).

        The program should output a single number - the number of days between the maximum and minimum dates of the entered sequence.     

'''
import sys
from datetime import datetime

DATE_FORMAT = '%Y-%m-%d'

def parse_iso_date(date_string):
    try:
        return datetime.strptime(date_string, DATE_FORMAT).date()
    except ValueError:
        raise ValueError('Invalid date format')    
    
def get_dates_from_input():
    # Get input lines and remove extra spaces
    dates = [line.strip() for line in sys.stdin.readlines()]
    # Convert strings to date objects
    return [parse_iso_date(date) for date in dates]   

def calculate_difference_between_min_and_max_dates(dates):
    return (max(dates) - min(dates)).days

dates = get_dates_from_input()
print(calculate_difference_between_min_and_max_dates(dates))