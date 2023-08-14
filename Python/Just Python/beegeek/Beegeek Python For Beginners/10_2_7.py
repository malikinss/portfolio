""" 
Task: The input to the program is a string of text. 
Write a program that removes from it all characters with indices 
divisible by 3, i.e. characters with indices 0, 3, 6, ....
"""

given_string = input()

for i in range(len(given_string)):
    if i % 3 != 0:
        print(given_string[i], end = '')