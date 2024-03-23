'''
TODO:   
        The birthday date is available to you.
        Complete the code below to output the following components:
            full name of the month in English
            full name of the day of the week in English
            year in YYYY format
            month number in MM format
            day of the month in DD format
'''
from datetime import date

birthday = date(1992, 10, 6)

print('name of the month:', birthday.strftime('%B'))
print('name of the weekday:', birthday.strftime('%A'))
print('year:', birthday.strftime('%Y'))
print('month:', birthday.strftime('%m'))
print('day:', birthday.strftime('%d'))
