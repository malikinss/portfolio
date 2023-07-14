""" 
Task: Given an odd natural number n.
Write a program that prints an isosceles star triangle with base n 
according to the example:

*
**
***
****
***
**
*

Note. Use a nested for loop.
"""

n = int(input())

for i in range(n):
    cur_cnt = (n // 2 + 1) - abs(n // 2 - i)
    
    for j in range(cur_cnt):
        print("*", end="")
    
    print()