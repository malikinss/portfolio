""" 
Task: The input to the program is a string of text. 
Write a program that checks if a string ends with the substring .com or .co.il.
"""

given_text = input()

if given_text.endswith('.com') or given_text.endswith('.co.il'):
    print('YES')
else:
    print('NO')