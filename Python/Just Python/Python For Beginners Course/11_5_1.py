""" 
Task: The input to the program is a string of text. 
Write a program that displays the words of the input 
string in a column.
"""

s = input()
lst = s.split()
print(*lst, sep = '\n')