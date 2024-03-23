'''
TODO:   
        A block of code in Python is given. 
        
        Write a program that deletes all lines in the given code that contain only comments. 
        
        If there is something else in the line besides the comment, then such a line does not need to be taken into account.
'''
import sys

def read_code_from_input():
    return [line for line in sys.stdin.readlines()]

def remove_comment_lines(code_snippet):
    return [line for line in code_snippet if not line.lstrip().startswith('#')]

def display_code(code_snippet):
    print(*code_snippet, sep='')

user_code = read_code_from_input()
updated_code = remove_comment_lines(user_code)
display_code(updated_code)