""" 
Task: Write a program that reads two integers and a string from the keyboard.
If this string represents one of the four mathematical operations (+, -, *, /), 
then print the result of applying this operation to the numbers entered earlier, otherwise print "Invalid operation".
If the user wants to divide by zero, display the text "You can't divide by zero!".
"""
number_1 = int(input())
number_2 = int(input())
operation = input()
if operation == "+":
    print(number_1 + number_2)
elif operation == "-":
    print(number_1 - number_2)
elif operation == "*":
    print(number_1 * number_2)
elif operation == "/":
    if number_2 != 0:
        print(number_1 / number_2)
    else:
        print("You can't divide by zero!")
else:
        print("Invalid operation")