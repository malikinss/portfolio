""" 
Task: The input to the program is a string of text. 
Write a program that cuts it into two equal parts, rearranges them, 
and displays them on the screen.
"""

string = input()
string_len = len(string)
mid_len = int(string_len/2)

if string_len % 2 != 0:
    mid_len += 1

string = string[mid_len:] + string[:mid_len]

print(string)