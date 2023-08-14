""" 
Task: Write a program that determines whether a user is allowed to access an Internet resource or not.

Input data format: is an integer — the age of the user.

Output format: The program should display the text "Access granted" if the age is at least 18, and "Access denied" otherwise.
"""
age = int(input())
if age >= 18:
    print('Access granted')
else:
    print('Access denied')