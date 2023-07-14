""" 
Task: Given a natural number n, (n≤ 9).
Write a program that prints a table of size n*5, where i-th line 
contains the number i (the numbers are separated by one space).
"""

n = int(input())

for i in range(1, n + 1):
    
    for j in range(5):
        print(i, end =' ')
    
    print() 