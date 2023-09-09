'''
TODO: A magic date is the date when the day multiplied by the month equals the number formed by the last two digits of the year.

Write a function is_magic(date) that takes a string representation of a valid date as an argument and returns True if the date is magic and False otherwise.
'''


def is_magic(date):
    seq = date.split(".")
    day, month, year = int(seq[0]), int(seq[1]), int(seq[2])
    
    return day * month == year % 100


date = input()

print(is_magic(date))