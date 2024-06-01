'''
TODO:
        Given a sequence of integers. 
        Write a program that determines whether a given sequence is a
        progression, and if so, determines its type.

        Input format:
            An arbitrary number of lines (at least three) are given as
            input to the program; each line contains a natural number -
            the next member of the sequence.

        Output format:
            The program should output the text:
                Arithmetic progression - if the entered sequence of
                numbers is an arithmetic progression

                Geometric progression - if the entered sequence of
                numbers is a geometric progression

                Not a progression - if the entered number sequence is
                not a progression

        Note 1: 
            It is guaranteed that the type of progression is uniquely
            determined.

        Note 2: 
            You can read more about arithmetic and geometric
            progressions here and here, respectively.
'''
import sys
from typing import List


def get_list_of_nums_from_input() -> List[str]:
    return [int(line.strip()) for line in sys.stdin.readlines()]


def is_arithmatic_progression(nums: List[int]):
    pass


def is_geometric_progression(nums: List[int]):
    pass


def print_progressions(nums: List[int]) -> None:
    if is_arithmatic_progression(nums):
        print('Arithmetic progression')
    elif is_geometric_progression(nums):
        print('Geometric progression')
    else:
        print('Not a progression')


def main() -> None:
    given_nums = read_input()
    print_dates_order(given_dates)


if __name__ == "__main__":
    main()
