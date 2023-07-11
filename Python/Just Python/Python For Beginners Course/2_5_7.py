""" 
Task: Write a program that calculates the sum and multiplication of the digits of a positive three-digit number.
"""
num = int(input())
digit_1 = num // 100
digit_2 = num // 10 % 10
digit_3 = num % 10
sum = digit_1 + digit_2 + digit_3
multiplication = digit_1 * digit_2 * digit_3
print('sum of digits =',sum)
print('multiplication of digits =',multiplication)