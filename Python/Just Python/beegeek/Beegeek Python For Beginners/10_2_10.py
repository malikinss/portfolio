""" 
Task: The input to the program is a string of text. 
Write a program that prints the index of the second occurrence 
of the letter "f". 
If the letter "f" occurs only once, print the number -1, and if 
it does not occur even once, print the number -2.
"""

given_string = input()

if given_string.count("f") == 0:
    print(-2)
elif given_string.count("f") == 1:
    print(-1)
else:
    res = given_string.replace("f", ".", 1).find("f")
    print(res)