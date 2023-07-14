""" 
Task: The input to the program is one line. 
Write a program that outputs:

the total number of characters in the line;
original string repeated 3 times;
the first character of the string;
the first three characters of the string;
the last three characters of the string;
line in reverse order;
a string with the first and last character removed.
"""

string = input()

# the total number of characters in the line
print(len(string))

# original string repeated 3 times
print(string * 3)

# the first character of the string
print(string[0])

# the first three characters of the string
print(string[:3])

# the last three characters of the string
print(string[-3:])

# line in reverse order
print(string[::-1])

# a string with the first and last character removed
print(string[1:][:-1])