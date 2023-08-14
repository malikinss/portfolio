""" 
Task: The program receives three strings as input: first name, 
last name, and patronymic. Write a program that prints out the 
initials of a person.
Note. It is guaranteed that the first name, last name and patronymic 
begin with a capital letter.
"""

first_name, last_name, middle_name = input(), input(), input()

print(last_name[0] + first_name[0] + middle_name[0])