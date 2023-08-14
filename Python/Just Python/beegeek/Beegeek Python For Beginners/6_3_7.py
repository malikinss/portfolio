""" 
Task: 
A regular polygon is a convex polygon in which all sides and all angles between adjacent sides are equal. The area of a regular polygon with side length a and number of sides n is calculated by the formula: S = (n*a^2)/4tg(pi/n)

Two numbers are given: a natural number n and a real number a. Write a program that finds the area of a given regular polygon.
"""

from math import *

n, a = float(input()), float(input())

S = (n * a**2)/(4*tan(pi/n))

print(S)