""" 
Task: The input to the program is a single number n.
Write a program that prints out a list of n English 
letters ['a', 'b', 'c', ...] in lowercase.
"""

n = int(input())

s = ""
for i in range(n):
    s += chr(ord("a") + i)
    
print(list(s))