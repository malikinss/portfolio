""" 
Task: The input to the program is a string of text consisting of 
words separated by exactly one space. 
Write a program that counts the number of words in it.
"""

given_string = input()

total = given_string.count(' ') + 1

print(total)