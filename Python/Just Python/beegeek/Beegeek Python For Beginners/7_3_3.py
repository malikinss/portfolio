""" 
Task: The input to the program is a natural number n. 
Write a program that evaluates the value of an expression
(1 + 1/2 + 1/3 + ... + 1/n) - ln(n)
"""

from math import log

n = int(input())
total = 0

for i in range(1, n + 1):
    total = total + (1 / i) 

print(total - log(n))