""" 
Task: The input to the program is a natural number n, 
and then n strings.
Write a program that creates a list of characters from all 
strings and then prints it out.
"""

n = int(input())
lst = []

for i in range(n):
    a = input()
    lst.extend(a)

print(lst)   