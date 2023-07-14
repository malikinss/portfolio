""" 
Task: Given a natural number n.
Write a program that prints a numerical triangle according to the example:

1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
16 17 18 19 20 21
...

Note. Use a nested for loop.
"""

n = int(input())
a = 1

for i in range(1, n + 1):
    for j in range(i):
        print(a, end=' ')
        a +=1 
    
    print()