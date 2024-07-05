'''
TODO:
        Implement a filter_dump() function that takes three arguments in
        the following order:
            filename — the name of the pickle file, such as data.pkl
            objects — a list of arbitrary objects
            typename — the type of data

        The function should create a pickle file named filename that contains
        a serialized list of only those objects in the objects list
        whose type is typename.
NOTE:
        For example, calling the filter_dump() function as follows:
            filter_dump('numbers.pkl', [1, '2', 3, 4, '5'], int)
        should create a file numbers.pkl containing the serialized list:
            [1, 3, 4].
'''
import pickle
from typing import List, Any, Type


def filter_objects_by_type(target_type: Type, objects: List[Any]) -> List[Any]:
    """
    Filters objects of the given list by the specified type.

    Args:
        target_type (Type): The type to filter elements by.
        objects (List[Any]): The list of objects to be filtered.

    Returns:
        List[Any]: A list containing only objects of the specified type.
    """
    return [obj for obj in objects if isinstance(obj, target_type)]


def create_pickle(data: Any, filename: str) -> None:
    """
    Serializes the given data to a pickle file.

    Args:
        data (Any): The data to be serialized.
        filename (str): The name of the pickle file.
    """
    with open(filename, mode='wb') as file:
        pickle.dump(data, file)


def filter_dump(filename: str, objects: List[Any], typename: Type) -> None:
    """
    Filters objects by type and serializes the result to a pickle file.

    Args:
        filename (str): The name of the pickle file.
        objects (List[Any]): The list of objects to be filtered.
        target_type (Type): The type to filter elements by.
    """
    # Filter the objects by the specified type
    filtered_objects = filter_objects_by_type(typename, objects)

    # Serialize the filtered objects to the specified pickle file
    create_pickle(filtered_objects, filename)
