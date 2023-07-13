""" 
Task: Write a program that reads one line and then outputs "YES"
if the input string contains the substring "Saturday" or "Sunday" 
and "NO" otherwise.
"""
input_string = input()

if 'Saturday' in input_string or 'Sunday' in input_string:
    print('YES')
else:
    print('NO')