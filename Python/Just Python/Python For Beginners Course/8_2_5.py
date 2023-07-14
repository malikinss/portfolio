""" 
Task: Given a natural number n, (n>99).
Write a program that determines its third (from the beginning) digit.
"""

n = int(input())

while n > 999:
    n //= 10

print(n % 10)