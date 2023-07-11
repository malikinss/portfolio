""" 
Task: Write a program that takes three positive numbers and determines 
if there exists a non-degenerate triangle with such sides.
"""
a = int(input())
b = int(input())
c = int(input())
if a < b + c and b < a + c and c < a + b:
    print('YES')
else:
    print('NO')