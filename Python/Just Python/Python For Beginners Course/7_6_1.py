""" 
Task: The number n>1 is given as input to the program.
Write a program that prints its smallest divisor other than 1.
"""

n = int(input())

for i in range(2, n + 1):
    if n % i == 0:
        print(i)
        break