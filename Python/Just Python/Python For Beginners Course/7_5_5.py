""" 
Task: Given a natural number n, (n>9).
Write a program that determines its second (from the beginning) digit.
"""

n = int(input())
while n > 99:
    n //= 10

second_digit = n % 10
print(second_digit)