""" 
Task: Write a program that reads a natural number n and prints the first n 
numbers of the Fibonacci sequence.
"""

n = int(input())
a, b = 1, 1

for i in range(n):
    print(a, end=' ')
    a, b = b, a + b