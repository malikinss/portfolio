""" 
Task: 
Three real numbers a, b, c are given. Write a program that finds the real roots of the quadratic equation ax^2+bx+c=0.
The program should print the real roots of the equation if they exist, or the text "No roots" otherwise.
Note. If the equation has two roots, then you should print them in ascending order.

"""
from math import *

a, b, c = float(input()), float(input()), float(input())

D = (b**2) - (4*a*c)

if D>0:
    x1 = ((-b) + sqrt(D))/(2*a)
    x2 = ((-b) - sqrt(D))/(2*a)
    
    if x1 > x2:
        print(x2)
        print(x1)
    elif x2 > x1:
        print(x1)
        print(x2)
        
elif D==0:
    x1 = (-b)/(2*a)
    print(x1)
    
else:
    print('No roots')