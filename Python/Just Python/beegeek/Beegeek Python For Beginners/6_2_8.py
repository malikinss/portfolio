""" 
Task: We will consider an email address to be valid if it 
contains the @ symbol and dots. 
Write a program that checks the correctness of an email address.
"""
given_email = input()

if ('.' in given_email) and ('@' in given_email):
    print('YES')
else:
    print('NO')