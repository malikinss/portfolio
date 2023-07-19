""" 
Task: The input to the program is a natural number n. 
Write a program that creates a list of divisors of a given number.
"""

n = int(input())
lst = []

for i in range(1,n+1):
    if n % i == 0:
        lst.append(i)

print(lst)   