""" 
Task: Write a program that reads two lines from the keyboard - the user's first and last name and outputs the phrase:

“Hello [first name entered] [last name entered]! You have just delved into Python.
"""
first_name = input()
last_name = input()

string_1 = 'Hello '
string_2 = ' '
string_3 = '! You just delved into Python'

output_sentence = string_1 + first_name + string_2 + last_name + string_3

print(output_sentence)