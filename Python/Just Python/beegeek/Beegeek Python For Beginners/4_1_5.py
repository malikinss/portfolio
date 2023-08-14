""" 
Task: Write a program that determines whether three given numbers (in the given order) are consecutive members of an arithmetic progression.
"""
a = int(input())
b = int(input())
c = int(input())
if a - b == b - c:
    print('YES')
else:
    print('NO')