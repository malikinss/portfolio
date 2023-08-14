""" 
Task: The input to the program is a natural number n.
Write a program that calculates n!.
"""

from math import factorial

n = int(input())

factorial_n = 1

for i in range(1, n + 1):
    factorial_n *= i

print(factorial_n)

#or

print(factorial(n))