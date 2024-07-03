'''
TODO:
        You have access to the data.json file, which contains a list of
        different objects:
            [
                "nwkWXma",
                null,
                {
                    "ISgHT": "dIUbf"
                },
                "Pzt",
                "BXcbGVTE",
                ...
            ]

        Write a program that creates a list whose elements are the objects
        from the list contained in the data.json file, modified according to
        the following rules:
            - if the object is a string, an exclamation mark is added
            to its end
            - if the object is a number, it is incremented by one
            - if the object is a boolean, it is inverted
            - if the object is a list, it is doubled
            - if the object is a JSON object (dictionary), a new pair
            "newkey": null is added to it
            - if the object is an empty value (null), it is not added

        The program should write the resulting list to the updated_data.json
        file.

NOTE:
        For example, if the data.json file was:
            ["Hello", 179, true, null, [1, 2, 3], {"key": "value"}]
        then the program would create a file updated_data.json with the
        following contents:
            ["Hello!", 180, false, [1, 2, 3, 1, 2, 3], {"key": "value", "newkey": null}]
'''
import json
from typing import List, Any, Dict


def read_json_data_from_file(file_path: str) -> List[Any]:
    """
    Read JSON data from a file.

    Args:
        file_path: Path to the JSON file.

    Returns:
        List containing JSON data.
    """
    with open(file_path, 'r', encoding='utf8') as file:
        return json.load(file)


def write_json_data_to_file(data: List[Any], file_path: str):
    """
    Write JSON data to a file.

    Args:
        data: JSON data to be written.
        file_path: Path to the output JSON file.
    """
    with open(file_path, 'w', encoding='utf8') as file:
        json.dump(data, file, ensure_ascii=False, indent=3)


def process_string_object(obj: str) -> str:
    """
    Process string object.

    Args:
        obj: String object.

    Returns:
        Processed string object.
    """
    return obj + '!'


def process_number_object(obj: int) -> int:
    """
    Process number object.

    Args:
        obj: Number object.

    Returns:
        Processed number object.
    """
    return obj + 1


def process_boolean_object(obj: bool) -> bool:
    """
    Process boolean object.

    Args:
        obj: Boolean object.

    Returns:
        Processed boolean object.
    """
    return not obj


def process_list_object(obj: List[Any]) -> List[Any]:
    """
    Process list object.

    Args:
        obj: List object.

    Returns:
        Processed list object.
    """
    return obj + obj


def process_dict_object(obj: Dict[str, Any]) -> Dict[str, Any]:
    """
    Process dictionary object.

    Args:
        obj: Dictionary object.

    Returns:
        Processed dictionary object.
    """
    obj["newkey"] = None
    return obj


def modify_data_objects(data: List[Any]) -> List[Any]:
    """
    Modify objects in a list according to specified rules.

    Args:
        data: List containing objects to be modified.

    Returns:
        List with modified objects.
    """
    object_processors = {
        str: process_string_object,
        int: process_number_object,
        bool: process_boolean_object,
        list: process_list_object,
        dict: process_dict_object
    }

    return [object_processors[type(obj)](obj) for obj in data if obj is not None]


input_file_path = 'data.json'
output_file_path = 'updated_data.json'

data = read_json_data_from_file(input_file_path)
modified_data = modify_data_objects(data)
write_json_data_to_file(modified_data, output_file_path)
