'''
TODO:   
        Write a program that takes an arbitrary number of lines and puts all the characters in reverse order on each line input.

NOTE:
        The order in which lines are output must match the order in which they were entered.

        If the program receives nothing as input, then it should output nothing.      

'''
import sys

def reversed_words_in_input():
    data = list(map(str.strip, sys.stdin))

    for row in data:
        reversed_row = row[-1::-1] + '\n'
        sys.stdout.writelines(reversed_row)

reversed_words_in_input()