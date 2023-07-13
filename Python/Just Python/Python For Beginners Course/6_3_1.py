""" 
Task: On a plane, the Euclidean distance between two points (x1; y1) and (x2; y2) 
is defined as p = sqrt((x1 - x2)^2 + (y1 - y2)^2)
Write a program that determines the Euclidean distance between two points whose coordinates are given.
"""
from math import pow, sqrt

x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())

squared_difference_x = pow(x1 - x2, 2)
squared_difference_y = pow(y1 - y2, 2)

distance = sqrt(squared_difference_x + squared_difference_y)

print(distance)