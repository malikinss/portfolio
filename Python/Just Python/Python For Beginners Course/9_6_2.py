""" 
Task: The input to the program is a string of text. 
Write a program that translates each of its characters into its 
corresponding code from the Unicode character table.
"""

given_string = input()

for i in range(len(given_string)):
    print(ord(given_string[i]), end = ' ')