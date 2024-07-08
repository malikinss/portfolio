'''
TODO:
        Implement a function called count_occurences() that takes two
        arguments in the following order:
            word — a word
            words — a sequence of words separated by spaces

        The function should determine how many times the word word occurs in
        the sequence words and return the result.

NOTE:
        The function should ignore case.
        That is, for example, the words Python and python are considered
        the same.
'''
from collections import Counter


def count_occurrences(word: str, words: str) -> int:
    """
    Determine how many times the word occurs in the sequence of words.

    Parameters:
    word (str): The word to count.
    words (str): A sequence of words separated by spaces.

    Returns:
    int: The number of occurrences of the word in the sequence of words.
    """
    word_count = Counter(words.lower().split())

    return word_count[word.lower()]


# Example usage
word = 'python'
words = 'Python Conferences python training python events'
print(count_occurrences(word, words))

word = 'Java'
words = 'Python C++ C# JavaScript Go Assembler'
print(count_occurrences(word, words))
