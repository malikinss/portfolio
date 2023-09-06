'''
TODO: Write a function get_days(month) that takes a month number as an argument and returns the number of days in a given month.

NOTE: It is guaranteed that the argument passed is in the range from 1 to 12. Consider the year to be a non-leap year.
'''

def get_days(month):
    if month in [1,3,5,7,8,10,12]:
        return 31
    elif month in [4,6,9,11]:
        return 30
    else:
        return 28


num = int(input())

print(get_days(num))