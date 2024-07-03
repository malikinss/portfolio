'''
TODO:
        You you have access to the food_services.json file, which contains a
        list of JSON objects that represent data on catering establishments:
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

        Write a program that:
            1) determines the district of Moscow in which the most
            establishments are located and outputs the name of this district
            and the number of establishments in it

            2) determines the chain with the largest number of establishments
            and outputs the name of this chain and the number of
            establishments in this chain

        The program should output the obtained values in the
        following format:
            <district>: <number of establishments>
            <name of the chain>: <number of establishments>

NOTE:
        It is guaranteed that the desired chain is unique.

        Example output:
            district Metrogorodok: 456
            French bakery SeDelice: 144
'''
import json
from typing import Dict, List, Any


def read_json_file(file_path: str) -> List[Dict[str, Any]]:
    """
    Read JSON data from a file.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        List[Dict[str, Any]]: List of dictionaries containing JSON data.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def increment_counter(counter: Dict[str, int], key: str) -> None:
    """
    Increment the counter for a given key.

    Args:
        counter (Dict[str, int]): Dictionary counter.
        key (str): Key to increment.
    """
    if key in counter:
        counter[key] += 1
    else:
        counter[key] = 1


def get_establishment_counts_by_district(establishments: List[Dict[str, Any]]) -> Dict[str, int]:
    """
    Get counts of establishments per district.

    Args:
        establishments (List[Dict[str, Any]]): List of establishments.

    Returns:
        Dict[str, int]: Counts of establishments per district.
    """
    district_counts = {}

    for establishment in establishments:
        district = establishment['District']
        increment_counter(district_counts, district)

    return district_counts


def get_establishment_counts_by_chain(establishments: List[Dict[str, Any]]) -> Dict[str, int]:
    """
    Get counts of establishments per chain.

    Args:
        establishments (List[Dict[str, Any]]): List of establishments.

    Returns:
        Dict[str, int]: Counts of establishments per chain.
    """
    chain_counts = {}

    for establishment in establishments:
        if establishment['IsNetObject'].lower() == 'да':
            chain_name = establishment['OperatingCompany']
            increment_counter(chain_counts, chain_name)

    return chain_counts


def get_key_by_value(d: Dict[str, Any], value: Any) -> str:
    """
    Find a key in dictionary by its value.

    Args:
        d (Dict[str, Any]): Dictionary to search.
        value (Any): Value to find.

    Returns:
        str: Key corresponding to the given value.
    """
    for key, val in d.items():
        if val == value:
            return key
    return ""


def print_max_item(counts: Dict[str, int]) -> None:
    """
    Print the item with the maximum count from a dictionary.

    Args:
        counts (Dict[str, int]): Dictionary of counts.
    """
    max_count = max(counts.values())
    item_name = get_key_by_value(counts, max_count)
    print(f'{item_name}: {max_count}')


if __name__ == "__main__":
    establishments_data = read_json_file('4_3_15/tests/food_services.json')

    district_counts = get_establishment_counts_by_district(establishments_data)
    chain_counts = get_establishment_counts_by_chain(establishments_data)

    print_max_item(district_counts)
    print_max_item(chain_counts)
