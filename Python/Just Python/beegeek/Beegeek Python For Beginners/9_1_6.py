""" 
Task: The input to the program is one string consisting of numbers. 
Write a program that calculates the sum of the digits in a given string.
"""

given_string = input()
total_sum = 0

for i in range(len(given_string)):
    total_sum += int(given_string[i])

print(total_sum)