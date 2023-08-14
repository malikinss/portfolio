""" 
Task: The input to the program is a natural number n, and then n integers. 
Write a program that creates a list from the given numbers, then removes 
all elements at odd indices, and then prints the resulting list.
"""

n = int(input())
lst = []

for i in range(n):
    a = int(input())
    lst.append(a)

del lst[1::2]

print(lst)