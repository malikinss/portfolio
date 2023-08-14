""" 
Task: Month number given (1,2,…, 12). 
Write a program that displays the number of days in this month. 
Assume that the year is not a leap year.
Note. Try to write the program in such a way that it has no more than three conditions.
"""
x = int(input())
if x == 2:
    print('28')
elif x == 4 or x == 6 or x == 9 or x == 11:
    print('30')
else:
    print('31')