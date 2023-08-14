""" 
Task: Given a natural number n.
Write a program that prints a numerical triangle according to the example:

1
22
333
4444
55555
...

Note. Use a nested for loop.
"""

n = int(input())

for i in range(1, n + 1):
    for j in range(i):
        print(i, end="")
    
    print()