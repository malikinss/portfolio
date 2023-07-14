""" 
Task: The input to the program is a natural number written in 
the decimal number system. 
Write a program that converts a given number to the binary number system.
"""

n = int(input())
res = ""

while n > 0:
    res = str(n % 2) + res
    n //= 2

print(res)