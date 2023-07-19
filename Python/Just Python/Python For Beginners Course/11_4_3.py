""" 
Task: When analyzing data collected as part of a scientific experiment, 
it can be useful to remove the largest and smallest value.

The input to the program is a natural number n, and then n different 
natural numbers.

Write a program that removes the smallest and largest values from given 
numbers, and then prints the remaining numbers each on a separate line 
without changing their order.
"""

n = int(input())
lst = []

for i in range(n):
    a = int(input())
    lst.append(a)

lst.remove(max(lst))
lst.remove(min(lst))

print(*lst, sep='\n')