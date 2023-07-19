""" 
Task: The input to the program is a string of text and a delimiter string. 
Write a program that inserts a specified separator between each character of an input string of text.
"""

string_1, string_2 = input(), input()
new_list = []

for i in range(len(string_1)):
    new_list.append(string_1[i])

output_string = string_2.join(new_list)

print(output_string)