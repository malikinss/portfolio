""" 
Task: Given a natural number n.
Write a program that prints a number triangle with a height of n, 
according to the example:

1
121
12321
1234321
123454321
...

Note. Use a nested for loop.
"""

n = int(input())

for i in range(1, n + 1):
    for j in range(1, i):
        print(j, end = "")

    print(i, end="")

    for j in range(i - 1, 0, -1):
        print(j, end = "")

    print()