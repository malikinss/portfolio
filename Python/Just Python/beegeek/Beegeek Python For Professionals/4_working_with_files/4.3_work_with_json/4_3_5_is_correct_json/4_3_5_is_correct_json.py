'''
TODO:
        Implement the is_correct_json() function that takes one argument:
            string — an arbitrary string

        The function should return True if the string is JSON-formatted, or
        False otherwise.
'''
import json


def is_correct_json(json_string: str) -> bool:
    """
    Check if the provided string is in valid JSON format.

    Args:
        json_string (str): The string to be checked.

    Returns:
        bool: True if the string is JSON-formatted, False otherwise.
    """
    try:
        json.loads(json_string)
        # If json.loads does not raise an exception, the string is valid JSON
        return True
    except ValueError:
        # If a ValueError is raised, the string is not valid JSON
        return False
