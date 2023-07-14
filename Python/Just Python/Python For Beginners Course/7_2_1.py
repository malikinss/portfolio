""" 
Task: Given two integers m and n, (m≤n).
Write a program that prints all numbers from m to n inclusive.
"""

m, n = int(input()), int(input())

for i in range(m, n+1):
    print(i)