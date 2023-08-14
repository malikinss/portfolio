""" 
Task: The input to the program is one line. 
Write a program that determines how many times + and * occur in a string.
"""

given_string = input()
cnt_plus = 0
cnt_mul = 0

for element in given_string:
    if element == "+":
        cnt_plus += 1
    elif element == "*":
        cnt_mul += 1

print("Symbol + occurs", cnt_plus, "times")
print("Symbol * occurs", cnt_mul, "times")