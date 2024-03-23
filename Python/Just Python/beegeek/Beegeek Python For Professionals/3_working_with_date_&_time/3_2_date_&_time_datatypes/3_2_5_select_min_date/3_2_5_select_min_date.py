'''
TODO:   
        Write a function that takes two dates as input and outputs the smaller one.

        The function receives two correct dates in ISO format (YYYY-MM-DD), each on a separate line.

        The function must select the smaller of the two entered dates and display it in DD-MM (YYYY) format.
'''
from datetime import date

def get_min_date(dates):
    return min(dates)

def input_dates(dates_number):
    return [date.fromisoformat(input()) for _ in range(dates_number)]

def select_min_date(dates_number):
    given_dates = input_dates(dates_number)

    min_date = get_min_date(given_dates)

    print(min_date.strftime('%d-%m (%Y)'))    
