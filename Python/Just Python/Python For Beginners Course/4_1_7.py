""" 
Task: Write a program that determines the smallest of four numbers.
"""
number1 = int(input())
number_2 = int(input())
number_3 = int(input())
number_4 = int(input())

if number1 > number_2:
    smallest_in_first_two = number_2
else:
    smallest_in_first_two = number1

if number_3 > number_4:
    smallest_in_second_two = number_4
else:
    smallest_in_second_two = number_3

if smallest_in_first_two > smallest_in_second_two:
    print(smallest_in_second_two)
else:
    print(smallest_in_first_two)