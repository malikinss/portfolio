""" 
Task: The program receives two natural numbers a and b (a< b) as input.
Write a program that finds a natural number from the interval [a; b] 
with the maximum sum of divisors.
If there are several such numbers, then print the largest of them.
"""

a, b = int(input()), int(input())

count = 0
large = 0

for i in range(a, b + 1):
    total = 0
    
    for j in range(1, i + 1):
        if i % j == 0:
            total += j
        
        if total >= count:
            count = total
            large = i

print(large, count)