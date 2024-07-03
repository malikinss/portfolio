'''
TODO:
        You have access to the people.json file, which contains a list of
        JSON objects.
        Moreover, different objects can have a different number of keys:
            [
                {
                    "age": 33,
                    "country": "Lesotho",
                    "phone": "(927) 316-2249",
                    "family_status": "married",
                    "email": "neonatus@outlook.com"
                },
                {
                    "age": 25,
                    "country": "Guinea",
                    "name": "Dorey",
                    "children": "yes",
                    "email": "ismail@gmail.com",
                    "university": "Khalifa University",
                    "family_status": "married"
                },
                ...
            ]

        Write a program that adds all missing keys to each JSON object from
        this list, assigning null to these keys.
        A key is considered missing if it is present in some other object, but
        is not present in this one.
        The program should create a list of updated JSON objects and write it
        to the updated_people.json file.

NOTE:
        The JSON objects in the list created by the program should be in their
        original order.

        The order of the keys in the JSON objects is not important.

        For example, if the people.json file was:
            [
                {
                    "age": 33,
                    "country": "Lesotho"
                },
                {
                    "age": 25,
                    "country": "Guinea",
                    "name": "Dorey"
                }
            ]
        then the program should create a file updated_people.json with the
        following contents:
            [
                {
                    "age": 33,
                    "country": "Lesotho"
                    "name": null
                },
                {
                    "age": 25,
                    "country": "Guinea",
                    "name": "Dorey"
                }
            ]
'''
import json
from typing import Dict, List


def read_json_file(file_path: str) -> List[Dict]:
    """
    Read JSON data from a file.

    Args:
        file_path: Path to the JSON file.

    Returns:
        List of dictionaries containing JSON data.
    """
    with open(file_path, 'r', encoding='utf8') as file:
        return json.load(file)


def write_json_file(data: List[Dict], file_path: str) -> None:
    """
    Write JSON data to a file.

    Args:
        data: JSON data to be written.
        file_path: Path to the output JSON file.
    """
    with open(file_path, 'w', encoding='utf8') as file:
        json.dump(data, file, ensure_ascii=False, indent=3)


def get_all_existing_keys(data: List[Dict]) -> set:
    """
    Get a set of all keys existing in a list of dictionaries.

    Args:
        data: List of dictionaries.

    Returns:
        A set containing all keys.
    """
    all_keys = set()

    for obj in data:
        all_keys.update(obj.keys())

    return all_keys


def add_missing_keys(data: List[Dict]) -> List[Dict]:
    """
    Add missing keys to each dictionary in a list, assigning None
    to missing keys.

    Args:
        data: List of dictionaries.

    Returns:
        List of dictionaries with missing keys added.
    """
    all_keys = get_all_existing_keys(data)

    for item in data:
        for key in all_keys:
            if key not in item:
                item[key] = None

    return data


if __name__ == "__main__":
    input_file_path = '4_3_9_/tests/people.json'
    output_file_path = '4_3_9_/tests/updated_people.json'

    # Read data from JSON file
    data = read_json_file(input_file_path)

    # Add missing keys to each dictionary in the list
    result_data = add_missing_keys(data)

    # Write updated data back to JSON file
    write_json_file(result_data, output_file_path)
