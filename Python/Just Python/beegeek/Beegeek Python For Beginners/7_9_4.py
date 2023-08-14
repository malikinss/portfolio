""" 
Task: The input to the program is a natural number n.
Write a program that displays a graphical representation of the 
divisibility of numbers from 1 to n inclusive.
In each line, you need to print the next number and as many “+” 
characters as there are divisors for this number.
"""

n = int(input())

for i in range(1, n + 1):
    count = 0
    
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1
    
    print(i, '+' * count, sep='')