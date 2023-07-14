""" 
Task: The input to the program is one line. 
Write a program that prints the message "Digit" (without quotes) 
if a string contains a digit. Otherwise, display the message 
"No digits" (without quotes).
"""

given_string = input()
digits = '0123456789'

for i in given_string:
    if i in digits:
        print('Цифра')
        break
else:
    print('Цифр нет')