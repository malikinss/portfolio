""" 
Task: The input to the program is a string of text. 
Write a program that counts the number of digits in a given string.
"""

text = input()
counter = 0

for i in range(10):
    counter += text.count(str(i))

print(counter)