""" 
Task: The input to the program is a string of text. 
Write a program that displays the character that appears most frequently 
on the screen.
Note 1. If there are several such characters, output the last character in order.
Note 2. It is necessary to distinguish between uppercase and lowercase letters, 
as well as letters of the Russian and English alphabets.
"""

given_text = input()

most_common = given_text[0]

for element in given_text:
    if given_text.count(element) >= given_text.count(most_common):
        most_common = element
        
print(most_common)