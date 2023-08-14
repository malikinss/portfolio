""" 
Task: The input to the program is a string of text. 
Write a program that determines whether a text tint is good or not. 
The text has a good tone if it contains the substring "good" in all possible cases.
The program should output "YES" if the text has a good hue and "NO" otherwise.
"""

given_string = input()

given_string = given_string.lower()
chk_string = 'good'

if chk_string in given_string:
    print('YES')
else:
    print('NO')