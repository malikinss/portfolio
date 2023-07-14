""" 
Task: The input to the program is two natural numbers a and b, (a< b).
Write a program that finds all prime numbers from a to b inclusive.
"""

a, b, = int(input()), int(input())

for cur_num in range(a, b + 1):
    if cur_num == 1:
        continue
    
    for i in range(2, cur_num):
        if cur_num % i == 0:
            break
    
    else:
        print(cur_num)