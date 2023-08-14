""" 
Task: Given two natural numbers m and n (m ≤ n).
Write a program that prints all numbers from m to n inclusive that 
satisfy at least one of the following conditions:

the number is divisible by 17 without a remainder;
the number ends in 9;
the number is divisible by 3 and 5 without a remainder at the same time.
"""

m, n = int(input()), int(input())

for i in range(m, n + 1):
    if (i % 10 == 9) or (i % 17 == 0) or (i % 15 == 0):
        print(i)