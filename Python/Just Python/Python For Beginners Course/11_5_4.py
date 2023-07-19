""" 
Task: The input to the program is a text string containing integers. 
Write a program that draws a bar chart given numbers.
"""

text = input().split()

for element in text:
    print("+" * int(element))