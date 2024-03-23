'''
TODO:   
        Hurricane Andrew, which struck Florida on August 24, 1992, was one of the costliest and deadliest hurricanes in U.S. history.

        Complete the code below to output the date August 24, 1992 in three different formats:
            - in YYYY-MM format
            - in the format month_name (YYYY), where month_name is the full name of the month in English
            - in the format YYYY-day_number, where day_number is the day of the year
'''
from datetime import date

andrew = date(1992, 8, 24)

print(andrew.strftime('%Y-%m'))     # display the date in YYYY-MM format
print(andrew.strftime('%B (%Y)'))   # display the date in month_name (YYYY) format
print(andrew.strftime('%Y-%j'))     # display the date in the format YYYY-day_number
