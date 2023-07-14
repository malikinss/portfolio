""" 
Task: The input to the program is a string consisting of the person's first and last name, separated by a single space. 
Write a program that checks that the first and last names begin with a capital letter.
"""

string_1 = input()
string_2 = string_1.title()

if string_1 == string_2:
    print('YES')
else:
    print('NO')