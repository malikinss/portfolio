'''
TODO:
        You have two files data1.json and data2.json, each containing a single
        JSON object:
        {
            "Holly-Anne": [
                33,
                "failed"
            ],
            "Caty": [
                36,
                "failed"
            ],
            ...
        }

        Write a program that merges two JSON objects into one JSON object, and
        if pairs from the first and second objects have matching keys, then
        the value should be taken from the second object.

        The program should write the resulting JSON object to the
        data_merge.json file.

NOTE:
        For example, if the files data1.json and data2.json were as follows:
        {
            "Timur": 99,
            "Anri": 97
        }
        {
            "Dima": 99,
            "Anri": 100
        }
        then the program would have to create a file data_merge.json with the
        following contents:
        {
            "Anri": 100,
            "Dima": 99,
            "Timur": 99
        }
        The elements in the resulting JSON object can be in any order.
'''
import json
from typing import Any, Dict


def read_json_file(file_path: str) -> Dict[str, Any]:
    """
    Read JSON data from a file.

    Args:
        file_path: Path to the JSON file.

    Returns:
        Dictionary containing JSON data.
    """
    with open(file_path, 'r', encoding='utf8') as file:
        return json.load(file)


def write_json_file(data: Dict[str, Any], file_path: str):
    """
    Write JSON data to a file.

    Args:
        data: JSON data to be written.
        file_path: Path to the output JSON file.
    """
    with open(file_path, 'w', encoding='utf8') as file:
        json.dump(data, file, ensure_ascii=False, indent=3)


def merge_data(data1: Dict[str, Any], data2: Dict[str, Any]) -> Dict[str, Any]:
    """
    Merge two dictionaries, preferring values from the second dictionary in
    case of key conflicts.

    Args:
        data1: The first dictionary.
        data2: The second dictionary.

    Returns:
        A merged dictionary.
    """
    merged_data = data1.copy()
    merged_data.update(data2)
    return merged_data


if __name__ == "__main__":
    input_file_path1 = 'data1.json'
    input_file_path2 = 'data2.json'
    output_file_path = 'data_merge.json'

    # Read data from JSON files
    data1 = read_json_file(input_file_path1)
    data2 = read_json_file(input_file_path2)

    # Merge the data
    merged_data = merge_data(data1, data2)

    # Write the merged data to a new JSON file
    write_json_file(merged_data, output_file_path)
