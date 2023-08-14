""" 
Task: The input to the program is two numbers a and b.
Write a program that, for each code value in the range a 
through b (inclusive), outputs its corresponding character 
from the Unicode character table.
"""

a, b = int(input()), int(input())

for i in range(a, b + 1):
    print(chr(i), end = ' ')