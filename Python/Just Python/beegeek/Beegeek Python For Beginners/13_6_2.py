'''
TODO: Write a function get_circle(radius) that takes the radius of a circle as an argument and returns two values: the length of the circle and the area of the circle bounded by the given circle.
'''


import math


def get_circle(radius):
    a = 2 * math.pi * radius
    b = radius**2 * math.pi
    
    return a, b


r = float(input())

length, square = get_circle(r)

print(length, square)