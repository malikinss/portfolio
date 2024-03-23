'''
TODO:   
        Write a program that will read the integer boundaries of the interval from the standard input (first the left one, then the right one, each on a separate line). 
        
        And then it will read integers from standard input until it encounters an empty line, which will mean the end of the input. 
        
        You will need to check whether all entered numbers are included in the interval; the check includes the boundaries of the interval.

INPUT:
        Integer values

OUTPUT:
        True/False
'''
import sys

def is_in_range(number, left_bound, right_bound):
    return left_bound <= number <= right_bound

def read_nums_from_input():
    return [int(line.strip()) for line in sys.stdin.readlines()]

def get_bounds():
    l_bound = int(input())
    r_bound = int(input())

    return l_bound, r_bound

left_bound, right_bound = get_bounds()    
nums = read_nums_from_input()

flags = []

for num in nums:
    flags.append(is_in_range(num, left_bound, right_bound))

print(all(flags))