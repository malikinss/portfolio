""" 
Task: The input to the program is a natural number n.
Write a program that calculates the sum of those numbers 
from 1 to n (inclusive) whose square ends in 2, 5, or 8.
If there are no such numbers in the specified range, then output 0.
"""

n = int(input())

total = 0

for i in range(5, n + 1, 10):
    total += i

print(total)