'''
TODO:
        Consider the following dictionary:
            {'a': [1, 2], 'b': [3, 1], 'c': [2]}

        Let's "flip" it, representing keys as values, and values as keys:
            {1: ['a', 'b'], 2: ['a', 'c'], 3: ['b']}

        Implement a flip_dict() function that takes one argument:
            dict_of_lists is a dictionary where the key is a number or string,
            and the value is a list of numbers or strings

        The function should return a new dictionary (of type defaultdict with
        type list as the default value), which is a "reversed" dictionary
        dict_of_lists.

NOTE:
        The keys in the dictionary returned by the function, as well as the
        elements in the lists, must be in their original order.
'''
from collections import defaultdict
from typing import Dict, List, DefaultDict, Union


def flip_dict(original_dict: Dict[Union[int, str], List[Union[int, str]]]) -> DefaultDict[Union[int, str], List[Union[int, str]]]:
    """
    Flips the dictionary by inverting keys and values.

    Args:
        original_dict (Dict[Union[int, str], List[Union[int, str]]]):
        A dictionary where the key is a number or string,
        and the value is a list of numbers or strings.

    Returns:
        DefaultDict[Union[int, str], List[Union[int, str]]]: A new dictionary
        with inverted keys and values.
    """
    flipped_dict = defaultdict(list)

    for key, values in original_dict.items():
        for value in values:
            flipped_dict[value].append(key)

    return flipped_dict


original_dict = {'a': [1, 2], 'b': [3, 1], 'c': [2]}
flipped_dict = flip_dict(original_dict)
print(flipped_dict)
