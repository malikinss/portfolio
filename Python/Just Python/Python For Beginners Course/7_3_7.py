""" 
Task: The input to the program is a natural number n. 
Write a program that calculates the sum of all its divisors.
"""

n = int(input())
sum_of_divs = 0

for i in range(1, n+1):
    if n % i == 0:
        sum_of_divs += i

print(sum_of_divs)