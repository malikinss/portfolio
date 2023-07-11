""" 
Task: Write a program to find the digits of a four digit number.
Input data format: The input to the program is a positive four-digit integer.
Output format: The program should display the text in accordance with the condition of the problem.
"""
num = int(input())
a = num // 1000
b = num // 100 % 10
c = num // 10 % 10
d = num % 10
print('The digit in the thousands position is', a)
print('The digit in the hundreds position is', b)
print('The digit in the tens position is', c)
print('The digit in the units position is', d)