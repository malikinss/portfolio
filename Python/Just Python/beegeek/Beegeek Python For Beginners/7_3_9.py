""" 
Task: The input to the program is a natural number n, and then n different 
natural numbers of the sequence, each on a separate line. 

Write a program that prints the largest and second largest number 
in a sequence.
"""

n = int(input())

max1, max2 = -1, -1

for _ in range(n):
    num = int(input())
    
    if num > max1:
        max2 = max1
        max1 = num
    elif num > max2:
        max2 = num
        
print(max1)
print(max2)