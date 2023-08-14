""" 
Task: Given a natural number.
Write a program that reverses the order of the digits of a number.
"""

num = int(input())
reversed_num = 0

while num != 0:
    last_digit = num % 10
    reversed_num += last_digit
    reversed_num *= 10
    num //= 10

reversed_num = int(reversed_num / 10)

print(reversed_num)