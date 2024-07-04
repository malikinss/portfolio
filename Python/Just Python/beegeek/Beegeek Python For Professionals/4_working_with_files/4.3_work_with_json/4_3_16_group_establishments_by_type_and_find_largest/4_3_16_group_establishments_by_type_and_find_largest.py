'''
TODO:
        you have access to the food_services.json file, which contains a list
        of JSON objects that represent data on catering establishments:
            [
                {
                    "Name": "SMETANA",
                    "IsNetObject": "no",
                    "OperatingCompany": "",
                    "TypeObject": "cafe",
                    "AdmArea": "North-Eastern Administrative Okrug",
                    "District": "Yaroslavl District",
                    "Address": "Moscow, Yegor Abakumov Street, Building 9",
                    "SeatsCount": 48
                },
                ...
            ]

        By "establishment" we mean one JSON object from this list.

        The establishment has the following attributes:
            Name — name
            IsNetObject — yes or no depending on whether the establishment
                          is a chain
            OperatingCompany — name of the chain
            TypeObject — type (cafe, canteen, restaurant, etc.)
            AdmArea — administrative zone
            District — district
            Address — full address
            SeatsCount — number of seats

        Write a program that identifies all types of establishments and for
        each type finds the largest establishment of this type (has the
        largest number of seats).

        The program should output all types of establishments in lexicographic
        order, indicating for each the largest establishment and the number of
        seats in it.

        The establishment data should be placed each on a separate line, in
        the following format:
            <type of establishment>: <name of establishment>, <number of seats>

NOTE:
        The initial part of the answer looks like this:
            bar: Bar association PROFSOYUZ, 800
            buffet: DINING - KANTINACITY, 320
            snack bar: Burger FARSH, 74
            ...
'''
import json
from typing import Dict, List, Any


def read_json_data(file_path: str) -> List[Dict[str, Any]]:
    """
    Read JSON data from a file.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        List[Dict[str, Any]]: List of dictionaries containing JSON data.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def group_establishments_by_type_and_find_largest(establishments: List[Dict[str, Any]]) -> Dict[str, List[Any]]:
    """
    Groups establishments by type and finds the largest establishment
    of each type.

    Args:
        establishments (List[Dict[str, Any]]): List of dictionaries
        representing establishments.

    Returns:
        Dict[str, List[Any]]: Dictionary where keys are establishment types,
        and values are lists of the name and seat count of the largest
        establishment of that type.
    """
    result = {}

    for establishment in establishments:
        establishment_type = establishment.get('TypeObject')
        establishment_name = establishment.get('Name')
        establishment_size = establishment.get('SeatsCount')

        if establishment_type not in result or establishment_size > result[establishment_type][1]:
            result[establishment_type] = [establishment_name, establishment_size]

    return dict(sorted(result.items()))


def print_establishments_results(data: Dict[str, List[Any]]) -> None:
    """
    Outputs results in the required format.

    Args:
        data (Dict[str, List[Any]]): Dictionary with grouped establishments.
    """
    for establishment_type, value in data.items():
        establishment_name, establishment_size = value

        print(f'{establishment_type}: {establishment_name}, {establishment_size}')


if __name__ == "__main__":
    establishments = read_json_data('4_3_16_group_establishments_by_type_and_find_largest/tests/food_services.json')
    result = group_establishments_by_type_and_find_largest(establishments)
    print_establishments_results(result)
