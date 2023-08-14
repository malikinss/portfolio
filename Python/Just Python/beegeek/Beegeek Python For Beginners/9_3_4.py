""" 
Task: The input to the program is a string. Write a program that counts 
the number of lowercase alphabetic characters.
"""

given_string, lower_cnt = input(), 0

for i in range(len(given_string)):
    if given_string[i].islower():
        lower_cnt += 1

print(lower_cnt) 