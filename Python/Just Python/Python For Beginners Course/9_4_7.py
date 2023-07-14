""" 
Task: The input to the program is a string of text.
If the letter "f" occurs only once in this string, print its index.
If it occurs two or more times, print the index of its first and 
last occurrence on the same line, separated by a space character.
If the letter "f" does not occur in the given string, print "NO".
"""

given_string = input()
counter = given_string.count("f")

if counter == 0:
    print("NO")
elif counter == 1:
    print(given_string.index("f"))
else:
    print(given_string.index("f"), given_string.rindex("f"))