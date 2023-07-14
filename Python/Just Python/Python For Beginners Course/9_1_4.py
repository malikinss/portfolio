""" 
Task: The input to the program is one line.
Write a program that prints the elements of a row in reverse order.
"""

given_string = input()

for i in range( -1 ,-len(given_string)-1, -1):
    print(given_string[i])