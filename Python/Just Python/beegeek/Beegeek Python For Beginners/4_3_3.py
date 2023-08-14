""" 
Task: Three distinct integers are given. 
Write a program that finds the average of a number.
The program should print the average of the number.
Note. The middle number is the number that will be the 
second if the three numbers are sorted in ascending order.
"""
a = int(input())
b = int(input())
c = int(input())
if a > b > c or c > b > a :
    print(b)
elif b > a > c or c > a > b:
    print(a)
else:
    print(c)