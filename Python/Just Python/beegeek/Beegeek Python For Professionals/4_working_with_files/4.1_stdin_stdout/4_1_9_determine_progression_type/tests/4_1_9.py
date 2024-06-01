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


def read_numbers_from_input() -> List[int]:
    """Reads a sequence of integers from standard input."""
    return [int(line.strip()) for line in sys.stdin.readlines()]


def is_arithmetic_progression(nums: List[int]) -> bool:
    """Checks if the sequence is an arithmetic progression."""
    if len(nums) < 2:
        return False
    common_difference = nums[1] - nums[0]
    return all(nums[i] - nums[i - 1] == common_difference for i in range(1, len(nums)))


def is_geometric_progression(nums: List[int]) -> bool:
    """Checks if the sequence is a geometric progression."""
    if len(nums) < 2 or nums[0] == 0:
        return False
    common_ratio = nums[1] / nums[0]
    return all(nums[i] / nums[i - 1] == common_ratio for i in range(1, len(nums)))


def determine_progression_type(nums: List[int]) -> None:
    if is_arithmetic_progression(nums):
        print('Arithmetic progression')
    elif is_geometric_progression(nums):
        print('Geometric progression')
    else:
        print('Not a progression')


def main() -> None:
    nums = read_numbers_from_input()
    determine_progression_type(nums)


if __name__ == "__main__":
    main()
