""" 
Task: Write a program to determine if a given year is a leap year. 
If the year is a leap year, then print "YES", otherwise print "NO".
A year is a leap year if its number is a multiple of 4 but not 
a multiple of 100, or if it is a multiple of 400.
"""
x = int(input())
if (x % 4 == 0 and x % 100 != 0) or x % 400 == 0:
    print('YES')
else:
    print('NO')