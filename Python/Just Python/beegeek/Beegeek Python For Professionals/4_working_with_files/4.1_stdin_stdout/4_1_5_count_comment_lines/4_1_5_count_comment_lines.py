'''
TODO:   
        A block of code in Python is given. 
        
        Write a program that determines the number of lines in a given code that contain only comments. 
        
        If there is something else in the line besides the comment, then such a line does not need to be taken into account.
'''
import sys

def read_code_from_input():
    code = [line.strip() for line in sys.stdin.readlines()]
    return code

def count_comment_lines(code_snippet):
    counter = 0

    for code_line in code_snippet:
        if code_line.startswith('#'):
            counter += 1

    return counter

print(count_comment_lines(read_code_from_input()))        