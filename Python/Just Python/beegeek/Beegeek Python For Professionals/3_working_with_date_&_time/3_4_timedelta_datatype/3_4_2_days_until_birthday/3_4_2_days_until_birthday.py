'''
TODO:   
        Complete the code below to print the number of days (integer) between the dates today and birthday.      
'''
from datetime import date

today = date(2021, 11, 4)
birthday = date(2022, 10, 6)

days = abs((today - birthday).days)

print(days)