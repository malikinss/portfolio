'''
TODO:
        You can access the text file pythonzen.txt, which contains the
        following text in English:
            The Zen of Python, by Tim Peters

            Beautiful is better than ugly.
            Explicit is better than implicit.
            ...

        Write a program that determines how many times each letter appears in
        this text.

        The letters and their counts should be printed in lexicographic order,
        each on a separate line, in the following format:
            <letter>: <count>

NOTE:
        The initial part of the answer looks like this:
            a: 53
            b: 21
            ...

        The program should not be case-sensitive, that is, for example, the
        letters a and A are considered the same.

        The program should ignore all non-alphabetic characters.
'''
from collections import Counter
import string


def read_lines_from_file(file_name: str) -> list[str]:
    """
    Reads lines from a text file and returns them as a list of strings.

    Args:
        file_name (str): The path to the text file.

    Returns:
        list[str]: A list of lines read from the file.
    """
    with open(file_name, 'rt', encoding='utf-8') as file:
        content = [line.rstrip() for line in file.readlines()]

    return content


def filter_letters_counter(counter: Counter) -> Counter:
    """
    Filters out non-alphabetic characters from a Counter object.

    Args:
        counter (Counter): Counter object containing character counts.

    Returns:
        Counter: Filtered Counter object with only alphabetic characters.
    """
    non_letters = [ch for ch in counter.keys() if ch not in string.ascii_letters]

    for non_letter in non_letters:
        del counter[non_letter]

    return counter


def count_letters(text: list[str]) -> dict[str, int]:
    """
    Counts the occurrences of each alphabetic letter in the given text.

    Args:
        text (list[str]): A list of strings representing the text.

    Returns:
        dict[str, int]: A dictionary mapping each letter to its count.
    """
    letter_counts = Counter()

    for line in text:
        letter_counts.update(line.lower())

    letter_counts = filter_letters_counter(letter_counts)

    return dict(sorted(letter_counts.items()))


def display_letter_counts(letter_counts: dict[str, int]) -> None:
    """
    Displays the counts of each letter in lexicographic order.

    Args:
        letter_counts (dict[str, int]): A dictionary mapping each letter to
        its count.

    Returns:
        None
    """
    for letter, count in letter_counts.items():
        print(f'{letter}: {count}')


if __name__ == "__main__":
    file_path = '6_7_5/tests/pythonzen.txt'
    data = read_lines_from_file(file_path)
    letter_counts = count_letters(data)
    display_letter_counts(letter_counts)
