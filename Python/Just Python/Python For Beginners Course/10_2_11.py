""" 
Task: The input to the program is a line of text in which 
the letter "h" occurs at least twice. 
Write a program that returns the original string and reverses 
the sequence of characters between the first and last 
occurrences of the letter "h".
"""

given_string = input()
occur_1 = given_string.find('h')
occur_2 = given_string.rfind('h')

result = given_string[:occur_1] + given_string[occur_2:occur_1:-1] + given_string[occur_2:]

print(result)