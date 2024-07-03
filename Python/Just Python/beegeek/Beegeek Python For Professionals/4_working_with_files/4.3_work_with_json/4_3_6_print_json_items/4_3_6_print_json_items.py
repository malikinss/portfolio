'''
TODO:
        Write a program that takes a description of one object in JSON format
        as input and outputs all key-value pairs of this object.

        Input:
            The program receives a valid description of one object in JSON
            format as input.

        Output:
            The program should output all key-value pairs of the input object,
            separating the key and value with a colon, each on a separate line.

        If the key value is a list, then all its elements should be output
        separated by commas.

NOTE:
        The key-value pairs must be in their original order when output.

        To read an arbitrary number of lines, use the sys.stdin stream input.
'''
import json
import sys
from typing import Dict, Any


def read_json_from_stdin() -> Dict[str, Any]:
    """
    Reads JSON data from standard input and returns it as a dictionary.

    Returns:
        dict: The JSON data as a dictionary.

    Raises:
        ValueError: If the input is not valid JSON.
    """
    try:
        data = json.loads(sys.stdin.read().strip())
        return data
    except json.JSONDecodeError as e:
        raise ValueError("Invalid JSON input") from e


def format_if_list(data: Any) -> Any:
    """
    Formats data if it's a list by joining its elements with commas.

    Args:
        data (Any): The data to format.

    Returns:
        Any: The formatted data if it's a list, otherwise the original data.
    """
    def is_list(data: Any) -> bool:
        return isinstance(data, list)

    return ', '.join(map(str, data)) if is_list(data) else data


def print_json_items(json_data: Dict[str, Any]) -> None:
    """
    Prints key-value pairs from the JSON data.

    Args:
        json_data (dict): The JSON data as a dictionary.
    """
    for key, value in json_data.items():
        formatted_value = format_if_list(value)
        print(f'{key}: {formatted_value}')


if __name__ == "__main__":
    data = read_json_from_stdin()
    print_json_items(data)
