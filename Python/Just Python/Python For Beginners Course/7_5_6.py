""" 
Task: Given a natural number. 
Write a program that determines if a given number 
consists of the same digits.
"""

n = int(input())
flag = "YES"
last_digit = n % 10

while n > 0:
    cur_digit = n % 10
    
    if last_digit != cur_digit:
        flag = "NO"

    n //= 10

print(flag)