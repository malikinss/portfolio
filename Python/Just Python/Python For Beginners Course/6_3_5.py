""" 
Task: 
Write a program that calculates the value ⌈x⌉+⌊x⌋ given a real number x.
Note. ⌈x⌉ - the ceiling of the number, ⌊x⌋ - the floor of the number.

"""
from math import *

x = float(input())

print(floor(x)+ceil(x))