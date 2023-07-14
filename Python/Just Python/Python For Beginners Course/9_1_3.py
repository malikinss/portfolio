""" 
Task: The input to the program is one line.
Write a program that displays the elements of a row 
with indices 0, 2, 4, ... in a column.
"""

given_string = input()

for i in range(0, len(given_string), 2):
    print(given_string[i])