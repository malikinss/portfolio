""" 
Task: Write a program that sorts three numbers from largest to smallest.
"""
a, b, c = int(input()), int(input()), int(input())

max_number = max(a, b, c)
min_number = min(a, b, c)
middle_number = a + b + c - min_number - max_number

print(max_number)
print(middle_number)
print(min_number)