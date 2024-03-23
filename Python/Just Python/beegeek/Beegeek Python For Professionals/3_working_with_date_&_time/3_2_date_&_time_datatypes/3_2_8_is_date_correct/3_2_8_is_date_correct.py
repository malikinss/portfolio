'''
TODO:   
        Implement a function is_correct() that takes three arguments in the following order:
            day — natural number, day
            month — natural number, month
            year — natural number, year

        The function must return True if the date with day, month and year components is valid, or False otherwise.
'''
from datetime import date

def is_correct(day, month, year):
    try:
        new_date = date(year, month, day)
        return True
    
    except ValueError:
        return False