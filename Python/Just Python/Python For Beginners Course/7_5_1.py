""" 
Task: Given a natural number.
Write a program that prints its digits in a column in reverse order.
"""

num = int(input())

while num != 0:
    last_digit = num % 10
    num = num // 10
    
    print(last_digit) 