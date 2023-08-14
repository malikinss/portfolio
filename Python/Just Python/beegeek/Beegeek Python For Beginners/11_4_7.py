""" 
Task: The input to the program is a natural number n, and then n integers. 
Write a program that first prints all negative numbers, then zeros, 
and then all positive numbers, each on a separate line. 
The numbers must be output in the same order in which they were entered.
"""

negatives, zeros, positives = [], [], []

n = int(input())

for _ in range(n):
    cur = int(input())
    if cur < 0:
        negatives.append(cur)
    elif cur > 0:
        positives.append(cur)
    else:
        zeros.append(cur)
        
res = negatives + zeros + positives
print(*res, sep="\n")