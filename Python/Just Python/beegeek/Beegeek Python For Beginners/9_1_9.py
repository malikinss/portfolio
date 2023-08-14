""" 
The input to the program is one line. 
Write a program that determines how many identical adjacent characters are in it.
"""

given_string = input()
count = 0

for i in range(1, len(given_string)):
    if given_string[i] == given_string[i-1]:
        count += 1

print(count)