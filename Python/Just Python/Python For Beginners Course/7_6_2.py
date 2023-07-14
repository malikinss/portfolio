""" 
Task: The input to the program is a natural number n.
Write a program that prints numbers from 1 to n inclusive except for:
numbers from 5 to 9 inclusive;
numbers from 17 to 37 inclusive;
numbers from 78 to 87 inclusive.
"""

n = int(input())
for i in range(1, n + 1):
    if (i > 4 and i < 10) or (i > 16 and i < 38) or (i > 77 and i < 88):
        continue
    
    print(i)