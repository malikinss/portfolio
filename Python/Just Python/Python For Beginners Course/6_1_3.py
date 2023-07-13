""" 
Task: Write a program that reads one number from the keyboard and prints its reciprocal. If at the same time the number entered from the keyboard is zero, then output "Reciprocal number does not exist" (without quotes).
"""
number = float(input())

if number == 0:
    print('Reciprocal number does not exist')
else:
    reciprocal = number ** (-1) 
    print(reciprocal)