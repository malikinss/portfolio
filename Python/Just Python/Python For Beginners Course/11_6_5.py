""" 
Task: The input to the program is a text string containing integers. 
A list of numbers is formed from this string. 
Write a program that sorts and prints the given list first in ascending order and then in descending order.
"""

seq = []
for el in input().split():
    seq.append(int(el))

seq.sort()
print(*seq)

seq.reverse()
print(*seq)