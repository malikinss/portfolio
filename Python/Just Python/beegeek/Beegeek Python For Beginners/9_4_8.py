""" 
Task: The input to the program is a line of text in which the letter "h" 
occurs at least twice. 
Write a program that removes the first and last occurrences of the letter "h" 
from this string, as well as all characters between them.
"""

given_string = input()

first = given_string.find("h")
last = given_string.rfind("h")
result = given_string[:first] + given_string[last+1:]

print(result)