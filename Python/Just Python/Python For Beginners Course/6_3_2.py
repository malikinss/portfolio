""" 
Task: Write a program that determines the area of a circle and the 
circumference of a circle given a given radius R.
"""
from math import pi, pow

R = float(input())

area = pi * pow(R, 2)
circumference = 2 * pi * R

print(area)
print(circumference)