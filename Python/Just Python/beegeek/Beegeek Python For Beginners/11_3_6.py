""" 
Task: The input to the program is a natural number n≥2, and then n integers.
Write a program that creates a list from the specified numbers, 
consisting of the sums of neighboring numbers (0 and 1, 1 and 2, 2 and 3, etc.).
"""

n = int(input())
a = int(input())
lst = []

for i in range(n-1):
    b = int(input())
    c = a + b
    a = b
    lst.append(c)

print(lst)