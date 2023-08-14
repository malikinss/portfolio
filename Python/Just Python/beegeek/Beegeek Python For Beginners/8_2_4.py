""" 
Task: The input to the program is a natural number n.
Write a program that prints an n*19 star frame.
"""

n = int(input())

for i in range(n):
    if i == 0 or i == (n - 1):
        cur_sep = "*"
    else:
        cur_sep = " "
        
    print("*", "*", sep = (cur_sep * 17))