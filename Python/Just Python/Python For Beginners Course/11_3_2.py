""" 
Task: The input to the program is a natural number n, and then n strings. 
Write a program that creates a list from the given strings and prints it out.
"""

n = int(input())
lst = []

for i in range(n):
    lst.append(input())

print(lst)