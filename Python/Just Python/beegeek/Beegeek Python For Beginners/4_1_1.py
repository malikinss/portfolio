""" 
Task: When registering on sites, you must enter your password twice. This is done for security, as this approach reduces the possibility of incorrect password entry.

Write a program that compares the password and its confirmation. If they match, then the program displays: "Password accepted", otherwise: "Password not accepted".
"""
password = input()
confirmation = input()
if password == confirmation:
    print('Password accepted')
else:
    print('Password not accepted')