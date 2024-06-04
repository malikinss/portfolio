'''
TODO:
        You have access to the wifi.csv file, which contains data on Moscow's
        city Wi-Fi.

        The first column contains the district name, the second column
        contains the name of the area, the third column contains the address,
        and the fourth column contains the number of access points
        at this address:
            adm_area;district;location;number_of_access_points
            Central Administrative District;Yakimanka District;Moscow, Serafimovich Street, Building 5/16;5
            Central Administrative District;Yakimanka District;Moscow, Bolotnaya Embankment, Building 11, Building 1;2
            ...

        Write a program that determines the number of access points in each
        district of Moscow and outputs the names of all districts, indicating
        the corresponding number of access points for each, each on a separate
        line, in the following format:
            <district name>: <number of access points>

        The names of the districts should be arranged in descending order of
        the number of access points; if the number of access points is the
        same, they should be arranged in lexicographic order.

NOTE:
        The delimiter in the wifi.csv file is a semicolon, and quotation marks
        are not used.

        When sorting, the names of the districts must be used exactly as they
        are specified in the original file.

        No additional transformations are required.
'''
import csv
from typing import List, Dict
from collections import defaultdict

FILE_TO_READ = '4_2_8/tests/wifi.csv'


def read_csv(filename: str, delimiter: str = ';') -> List[Dict[str, str]]:
    """Reads a CSV file and returns its content as a list of dictionaries.

    Args:
        filename (str):
            The path to the CSV file.
        delimiter (str):
            The delimiter used in the CSV file.

    Returns:
        List[Dict[str, str]]:
            The content of the CSV file.
    """
    with open(filename, 'r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=delimiter)
        return [row for row in reader]


def count_access_points_per_district(data: List[Dict[str, str]]) -> Dict[str, int]:
    """
    Counts the number of access points per district.

    Args:
        data (List[Dict[str, str]]):
            The list of dictionaries containing the data.

    Returns:
        Dict[str, int]:
            A dictionary with district names as keys and the
        number of access points as values.
    """
    access_points_per_district = defaultdict(int)

    for record in data:
        district = record['district']
        num_points = int(record['number_of_access_points'])
        access_points_per_district[district] += num_points

    return access_points_per_district


def print_access_points_per_district(num_access_points_per_district: Dict[str, int]) -> None:
    """
    Prints the number of access points per district in descending order.

    Args:
        num_access_points_per_district (Dict[str, int]):
            A dictionary with district names as keys and the number of access
            points as values.
    """
    sorted_districts = sorted(num_access_points_per_district.items(), key=lambda x: (-x[1], x[0]))
    for district, number in sorted_districts:
        print(f'{district}: {number}')


# Read data from CSV file
data = read_csv(FILE_TO_READ)
# Get the number of access points per district
number_per_district = count_access_points_per_district(data)
# Print the number of access points per district
print_access_points_per_district(number_per_district)
