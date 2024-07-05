'''
TODO:
        A pickle file containing a serialized dictionary or list is
        transmitted over a communication channel, and an integer
        — a checksum, which is calculated according to the following rule:
            1) for a dictionary — the sum of all integer keys (type int)
            2) for a list — the product of the minimum and maximum integer
               elements (type int)

        Write a program that calculates the checksum for an object contained
        in a pickle file and compares it with a given integer.

        The program receives the name of the pickle file containing the
        serialized dictionary or list in the first line, and an integer
        in the next line.

        The program should calculate the checksum for the object contained in
        the given pickle file, and if it matches the entered number,
        output the text:
            Checksums match

        if it does not match the entered number, output the text:
            Checksums do not match

NOTE:
        If the list (dictionary) does not contain integer elements (keys),
        then consider the checksum to be 0.

        Let's consider the first test.
        The file name is given — data.pkl, which contains the serialized list:
            ['a', 'b', 3, 4, 'f', 'g', 7, 8]

        then the number — 3023.

        The checksum for this list is 3⋅8=24.
        Since 3023 ≠ 24, the program outputs:
            Checksums do not match
'''
import pickle
from typing import List, Dict, Any, Union


def deserialize_pickle_file(pickle_file_path: str) -> Union[Dict[Any, Any], List[Any]]:
    """
    Deserializes an object from the given pickle file.

    Args:
        pickle_file_path (str): Path to the pickle file.

    Returns:
        Union[Dict[Any, Any], List[Any]]: The deserialized dictionary or list.
    """
    with open(pickle_file_path, 'rb') as file:
        return pickle.load(file)


def extract_integer_elements(items: Union[List[Any], Dict[Any, Any]]) -> List[int]:
    """
    Extracts all integer elements from a list or integer keys
    from a dictionary.

    Args:
        items (Union[List[Any], Dict[Any, Any]]): A list or dictionary
        containing various elements.

    Returns:
        List[int]: A list containing only integer elements or keys.
    """
    if isinstance(items, list):
        return [item for item in items if isinstance(item, int)]
    elif isinstance(items, dict):
        return [key for key in items.keys() if isinstance(key, int)]
    return []


def calculate_checksum(data_structure: Union[Dict[Any, Any], List[Any]]) -> int:
    """
    Calculates the checksum for the given data structure.

    Args:
        data_structure (Union[Dict[Any, Any], List[Any]]): The data structure
        to calculate the checksum for.

    Returns:
        int: The calculated checksum.
    """
    integer_elements = extract_integer_elements(data_structure)

    if isinstance(data_structure, list) and integer_elements:
        return min(integer_elements) * max(integer_elements)
    elif isinstance(data_structure, dict) and integer_elements:
        return sum(integer_elements)

    return 0


def compare_and_print_checksum(expected_checksum: int,
                               calculated_checksum: int) -> None:
    """
    Compares the expected checksum with the calculated checksum and prints
    the result.

    Args:
        expected_checksum (int): The expected checksum.
        calculated_checksum (int): The calculated checksum.
    """
    if expected_checksum == calculated_checksum:
        print('Контрольные суммы совпадают')
    else:
        print('Контрольные суммы не совпадают')


if __name__ == '__main__':
    pickle_file_path = input()
    expected_checksum = int(input())

    data_structure = deserialize_pickle_file(pickle_file_path)

    calculated_checksum = calculate_checksum(data_structure)

    compare_and_print_checksum(expected_checksum, calculated_checksum)
