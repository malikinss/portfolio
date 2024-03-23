'''
TODO:   
        Implement a function saturdays_between_two_dates() that takes two arguments in the following order:
        
            start — start date, date type
            end — end date, date type

        The function must return the number of Saturdays between the start and end dates, inclusive.       

NOTE:   
        Dates can be transmitted in any order, that is, it is not guaranteed that the first date is less than the second.

'''
from datetime import date


def is_saturday(given_date):
    return given_date.weekday() == 5
    
def saturdays_between_two_dates(date_1, date_2):
    saturdays_counter = 0

    # Convert dates to their ordinal number
    date_1_ord = date_1.toordinal()
    date_2_ord = date_2.toordinal()

    if date_1_ord > date_2_ord:
        date_1_ord, date_2_ord = date_2_ord, date_1_ord

    # Enumerate days between two dates (inclusive)
    for current_date_ordinal in range(date_1_ord, date_2_ord+1):
        # Convert sequence number back to date
        current_date = date.fromordinal(current_date_ordinal)

        if is_saturday(current_date):
            saturdays_counter += 1

    return saturdays_counter
