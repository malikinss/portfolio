""" 
Task: Write a program that determines if a year with a given number ends in two zeros. If the year ends, then print "YES", otherwise print "NO".
"""
year = int(input())
a = year % 100
a = a//10
b = year % 10
if a == 0 and b == 0:
    print('YES')
else:
    print('NO')