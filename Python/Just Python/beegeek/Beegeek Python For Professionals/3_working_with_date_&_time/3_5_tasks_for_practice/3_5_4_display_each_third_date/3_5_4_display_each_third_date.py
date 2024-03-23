'''
TODO:   
       Two dates are given - the left and right boundaries of the range, respectively. 
       
       Write a program that, from this range, including boundaries, prints, starting from a date for which the sum of the day and month is odd, every third date, only if it is not Monday or Thursday.

       The program receives two dates as input in the format DD.MM.YYYY - the left and right boundaries of the range, respectively, each on a separate line. 
       
       It is guaranteed that the first date is not greater than the second.

       The program must, from the specified range, including the ends, output, starting from a date for which the sum of the day and month is odd, every third date, only if it is not Monday or Thursday. 
       
       Each date must be located on a separate line, in the format DD.MM.YYYY

NOTE:
        If there are no dates that satisfy the condition, the program should not output anything.
'''

from datetime import datetime, timedelta

DATE_FORMAT = '%d.%m.%Y'
    
def parse_date(date_string):
    try:
        return datetime.strptime(date_string, DATE_FORMAT).date()
    except ValueError:
        raise ValueError('Invalid datetime format. Please use the format DD.MM.YYYY HH:MM')       

def is_odd(number):
    return 0 != number % 2

def sum_of_day_and_month_in_date(given_date):
    return int(given_date.day + given_date.month)

def find_first_odd_sum_day_month_in_range(start_date, end_date):
    current_date = start_date

    while current_date <= end_date:
        if is_odd(sum_of_day_and_month_in_date(current_date)):
            return current_date

        current_date += timedelta(days=1)    

def display_date(given_date):
    print(given_date.strftime(DATE_FORMAT))

def is_not_monday_or_thursday(given_date):
    return given_date.weekday() not in (0,3) 
    
def display_each_third_date_if_not_monday_and_thursday():
    left_border_date = parse_date(input())
    right_border_date = parse_date(input()) + timedelta(days=1)

    current_date = find_first_odd_sum_day_month_in_range(left_border_date, right_border_date)

    while current_date < right_border_date:
        if is_not_monday_or_thursday(current_date):
            display_date(current_date)

        current_date += timedelta(days=3)     

display_each_third_date_if_not_monday_and_thursday()