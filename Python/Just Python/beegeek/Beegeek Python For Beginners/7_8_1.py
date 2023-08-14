""" 
Task: Given a natural number n, (n≤ 9).
Write a program that prints an n*3 table consisting of a given number 
(the numbers are separated by a single space).
"""

n = int(input())

for i in range(n):
    
    for j in range(3):
        print(n, end =' ')
    
    print()  