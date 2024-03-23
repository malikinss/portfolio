'''
TODO:   
        Implement a function get_date_range() that takes two arguments in the following order:
            start — start date, date type
            end — end date, date type

        The get_date_range() function must return a list of dates (type date) from start to end inclusive.

        If start > end, the function should return an empty list.
'''
from datetime import date

def get_date_range(start, end):
    return [date.fromordinal(i) for i in range(start.toordinal(), end.toordinal() + 1)]