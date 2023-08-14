""" 
Task: Write a program that takes three positive numbers 
and determines the type of triangle whose side lengths 
are equal to the given numbers.

The program should display text on the screen - a type of 
triangle ("Equilateral", "Isosceles" or "Scales").
"""
a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print('Equilateral')
elif a == b or a == c or b == c:
    print('Isosceles')
else:
    print('Scales')