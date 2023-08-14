""" 
Task: Write a program that, given the user's age, tells what age group he belongs to:

up to 13 inclusive - childhood;
from 14 to 24 - youth;
from 25 to 59 - maturity;
from 60 - old age.
Input data format
The input to the program is a single integer - the age of the user.

Output format
The program should display the name of the age group.
"""
age = int(input())
if age <= 13:
    print('childhood')
else:
    if age <= 24:
        print('youth')
    else:
        if age <= 59:
            print('maturity')
        else:
            print('old age')