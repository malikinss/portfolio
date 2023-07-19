""" 
Task: The input to the program is a text string containing the name, patronymic and surname of the person. 
Write a program that prints out the initials of a person.
"""

full_name = input().split()

print(full_name[0][0], full_name[1][0], full_name[2][0], sep=".", end=".")