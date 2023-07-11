""" 
Task: We call a number beautiful if it has four digits and is evenly divisible by 7 or 17. 
Write a program that determines whether the entered number is beautiful. 
The program should output "YES" if the number is pretty, or "NO" otherwise.
"""
x = int(input())
if 999 < x < 10000 and ( x % 7 == 0 or x % 17 == 0 ):
    print('YES')
else:
    print('NO')