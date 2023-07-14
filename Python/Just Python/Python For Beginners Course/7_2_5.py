""" 
Task: Given a natural number n.
Write a program that prints the multiplication table for n 
(from 1 to 10 inclusive).
"""

n = int(input())

for i in range(1, 11):
    result = i * n
    print(n, 'x', i, '=', result)