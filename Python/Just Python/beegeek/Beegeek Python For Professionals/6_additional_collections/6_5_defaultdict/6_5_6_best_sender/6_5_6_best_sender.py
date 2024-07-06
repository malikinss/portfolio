'''
TODO:
        Consider two lists:
            messages = ['Hi, Linda', 'Hi, Sam', 'How are you doing?']
            senders = ['Sam Fisher', 'Linda', 'Sam Fisher']

        The first list represents a set of sent messages in some messenger,
        the second list is a set of senders of these messages.

        And the message messages[i] was sent by the user senders[i].

        Each message is a sequence of words separated by a space (punctuation
        marks are considered parts of words).

        The number of words is the total number of words sent by the user.

        Note that each user can send more than one message.

        For example, the user Sam Fisher sent 2 words in the first message and
        4 words in the second, therefore, his number of words is 2+4=6.

        Implement a function best_sender() that takes two arguments in
        the following order:
            messages — a list of messages
            senders — a list of sender names

        The function should determine the sender with the largest number of
        words and return its name.

        If there are multiple such senders, the name of the one whose name is
        greater in a lexicographic comparison should be returned.

NOTE:
        It is guaranteed that the lengths of the lists passed to the function
        are the same.
'''
from collections import defaultdict
from typing import List, Dict


def count_words_per_sender(messages: List[str],
                           senders: List[str]) -> Dict[str, int]:
    """
    Counts the number of words sent by each sender.

    Args:
        messages (List[str]): A list of messages.
        senders (List[str]): A list of senders corresponding to the messages.

    Returns:
        Dict[str, int]: A dictionary with the sender's name as the key and the
        total word count as the value.
    """
    word_count_per_sender = defaultdict(int)

    for message, sender in zip(messages, senders):
        word_count_per_sender[sender] += len(message.split())

    return word_count_per_sender


def find_best_sender(amount_per_sender: Dict[str, int]) -> str:
    """
    Finds the sender with the largest number of words.
    If there are multiple such senders, returns the one with the
    lexicographically greatest name.

    Args:
        word_count_per_sender (Dict[str, int]): A dictionary with the sender's
        name as the key and the total word count as the value.

    Returns:
        str: The name of the sender with the largest number of words.
    """
    return max(amount_per_sender, key=lambda sender: (amount_per_sender[sender], sender))


def best_sender(messages: List[str], senders: List[str]) -> str:
    """
    Determines the sender with the largest number of words and returns their
    name.
    If there are multiple such senders, the name of the one whose name is
    greater
    in a lexicographic comparison is returned.

    Args:
        messages (List[str]): A list of messages.
        senders (List[str]): A list of senders corresponding to the messages.

    Returns:
        str: The name of the sender with the largest number of words.
    """
    word_count_per_sender = count_words_per_sender(messages, senders)

    return find_best_sender(word_count_per_sender)


messages = ['Hi, Linda', 'Hi, Sam', 'How are you doing?']
senders = ['Sam Fisher', 'Linda', 'Sam Fisher']

print(best_sender(messages, senders))
