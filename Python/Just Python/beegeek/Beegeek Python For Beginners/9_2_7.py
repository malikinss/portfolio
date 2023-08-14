""" 
Task: The input to the program is one line. 
Write a program that outputs:

the third character of this line;
penultimate character of this line;
the first five characters of this string;
the entire line, except for the last two characters;
all characters with even indices;
all characters with odd indices;
all characters in reverse order;
all characters of the string through one in reverse order, 
starting with the last one.
"""

string = input()

# the third character of this line
print(string[2])

# penultimate character of this line
print(string[-2])

# the first five characters of this string
print(string[:5])

# the entire line, except for the last two characters
print(string[:-2])

# all characters with even indices
print(string[::2])

# all characters with odd indices
print(string[1::2])

# all characters in reverse order
print(string[::-1])

# all characters of the string through one in reverse order, starting with the last one
print(string[::-1][::2])