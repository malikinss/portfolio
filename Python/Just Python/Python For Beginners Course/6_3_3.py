""" 
Task: In mathematics, the following averages are distinguished:

arithmetic mean of numbers a and b: (a+b)/2
geometric mean of numbers a and b: sqrt(a*b)
harmonic mean of numbers a and b: (2*a*b)/(a+b)
quadratic mean  of numbers a and b: sqrt((a^2 + b^2)/2)

The program should display 4 numbers: arithmetic mean, geometric mean, harmonic and quadratic.
"""
from math import sqrt

a, b = float(input()), float(input())

arithmetic_mean = (a + b) / 2

geometric_mean = sqrt(a * b)

harmonic_mean = 2 / ((1 / a) + (1 / b))

quadratic_mean = sqrt((a ** 2 + b ** 2) / 2)

print(arithmetic_mean)
print(geometric_mean)
print(harmonic_mean)
print(quadratic_mean)