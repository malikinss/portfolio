""" 
Task: Write a program that reads a sequence of 10 integers and 
determines whether each of them is even or not.
The program should output the string "YES" if all numbers are even 
and "NO" otherwise.
"""

counter = 0

for _ in range(10):
    num = int(input())
    
    if num % 2 == 0:
        counter += 1

if counter == 10:
    print('YES')
else:
    print('NO')