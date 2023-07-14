""" 
Task: Given a natural number n, (n ≤ 9).
Write a program that prints an addition table for all numbers 
from 1 to n (inclusive) according to the example.
"""

n = int(input())

for i in range(1, n + 1):
    
    for j in range(1, 10):
        a = i + j
        print(i, '+', j, '=', a)
    
    print() 