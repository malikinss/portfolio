""" 
Task: The input to the program is a text string containing 4 positive integers separated by a dot. 

Write a program that determines if an input string of text is a valid ip address.
"""

text = input().split(".")

for element in text:
    if not (0 <= int(element) <= 255):
        print("NO")
        break
else:
    print("YES")