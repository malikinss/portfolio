'''
TODO:   
        A date is considered “interesting” if its year coincides with the user's year of birth, and the sum of the month number and day number is equal to his age.

        Implement a function print_good_dates() that takes one argument:
            dates — list of dates (date type)

        The function should display “interesting” dates in ascending order, each on a separate line, in the format month_name DD, YYYY, where month_name is the full name of the month in English.

NOTE:
        If an empty list or a list with no interesting dates is passed to the function, the function should not output anything.
'''
from datetime import date

USER_BIRTHYEAR = 1992
USER_AGE = 29

def format_output_dates(dates):
    return [current_date.strftime('%B %d, %Y') for current_date in dates]

def get_good_dates(dates):
    good_dates = []

    for current_date in dates:
        condition_1 = current_date.year == USER_BIRTHYEAR
        condition_2 = (current_date.month + current_date.day) == USER_AGE

        if condition_1 and condition_2:
            good_dates.append(current_date)

    return good_dates

def print_good_dates(dates):
    good_dates = get_good_dates(dates)
    formated_good_dates = format_output_dates(sorted(good_dates))
    
    print(*formated_good_dates, sep='\n')