""" 
Task: Write a program that reads three numbers and calculates the 
sum of only positive numbers.
Input data format: The program receives three integers as input.
Output format: The program should output one number - the sum of 
positive numbers.
Note. If there are no positive numbers, then print 0.
"""
number_1 = int(input())
number_2 = int(input())
number_3 = int(input())

if  number_1 <= 0:
    number_1 = 0

if  number_2 <= 0:
    number_2 = 0

if  number_3 <= 0:
    number_3 = 0
    
print(number_1+number_2+number_3)