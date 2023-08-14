""" 
Task: The input to the program is a natural number n, and then n strings.

Write a program that prints only unique strings, in the same order they were entered.
"""

n = int(input())
lst = []

for i in range(n):
    a = input()
    
    if a not in lst:
        lst.append(a)

print(*lst, sep = '\n')