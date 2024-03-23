'''
TODO:   
        A sequence of non-negative integers is given. 

        Write a program that outputs the numbers that occur more than once in a given sequence.

NOTE:   
        The program should print those numbers that appear more than once in a given line, separating them with a space. 
        Numbers must be arranged in ascending order and must not be repeated.
        If there are no duplicate numbers in the source string, the program should not output anything.
'''
from collections import defaultdict

def convert_sequence_to_integers_list(sequence):
    """Converts a space-separated sequence of integers into a list of integers."""
    return list(map(int, sequence.split()))

def generate_number_occurrence_counter(numbers):
    """
    Generates a dictionary counting the occurrences of each number in the list.

    :param numbers: List of integers
    :return: Dictionary with number occurrences
    """
    occurrences = defaultdict(int)

    for number in numbers:
        occurrences[number] += 1

    return occurrences

def get_duplicates_list(occurrences):
    """
    Extracts a list of numbers that occur more than once from the occurrences dictionary.

    :param occurrences: Dictionary with number occurrences
    :return: List of numbers occurring more than once
    """
    duplicates = [key for key, value in occurrences.items() if value >= 2]
    return duplicates
        
def find_duplicate_numbers(sequence):
    """
    Finds and returns a sorted list of numbers that occur more than once in the given sequence.

    :param sequence: Input sequence of integers
    :return: Sorted list of duplicate numbers
    """
    numbers = convert_sequence_to_integers_list(sequence)
    numbers_occurrences = generate_number_occurrence_counter(numbers)
    duplicate_numbers = get_duplicates_list(numbers_occurrences)

    return sorted(duplicate_numbers)


# Take user input and print the result
user_input = input("Enter a sequence of non-negative integers: ")
result = find_duplicate_numbers(user_input)
print(*result)