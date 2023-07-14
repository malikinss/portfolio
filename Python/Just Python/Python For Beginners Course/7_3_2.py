""" 
Task: The input to the program is a natural number n, 
and then n integers, each on a separate line. 
Write a program that calculates the sum of the given numbers.
"""

n = int(input())
total = 0

for i in range(n):
    total += int(input())

print(total)