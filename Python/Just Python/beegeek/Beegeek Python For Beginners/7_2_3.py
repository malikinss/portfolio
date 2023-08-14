""" 
Task: Two integers m and n (m > n) are given.
Write a program that prints all odd numbers from m to n inclusive
in descending order.
"""

m, n = int(input()), int(input())

for i in range(m, n - 1, -1):
    if i % 2 != 0:
        print(i)