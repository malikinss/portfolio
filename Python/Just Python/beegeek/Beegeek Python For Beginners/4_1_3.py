""" 
Task: Write a program that checks that for a given four-digit number the following relationship holds: the sum of the first and last digits is equal to the difference between the second and third digits.
"""
number = int(input())
digit_1 = number // 1000
digit_2 = number // 100 % 10
digit_3 = number // 10 % 10 
digit_4 = number  % 10
if (digit_1 + digit_4) == (digit_2 - digit_3):
    print('YES')
else:
    print('NO')