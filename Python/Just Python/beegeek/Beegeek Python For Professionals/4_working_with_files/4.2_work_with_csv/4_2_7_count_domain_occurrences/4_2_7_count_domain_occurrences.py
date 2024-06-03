'''
TODO:
        You have access to the data.csv file, which contains unique data about
        users of a certain resource.

        The first column contains the user's name, the second column contains
        the last name, and the third column contains the email address:
            first_name,surname,email
            John,Wilson,johnwilson@outlook.com
            Mary,Wilson,marywilson@list.ru
            ...

        Write a program that creates a domain_usage.csv file with the
        following contents:
            domain,count
            rambler.ru,24
            iCloud.com,29
            ...
        where the first column contains the name of the mail domain, and the
        second column contains the number of users using this domain.

        The domains in the file must be arranged in ascending order of the
        number of their uses, or in lexicographic order if the number of
        uses is the same.

NOTE:
        The comma is the separator in the data.csv file, and quotation marks
        are not used.
'''
import csv
from typing import List, Dict, Any

FILE_TO_READ = '4_2_7/tests/data.csv'
FILE_TO_WRITE = '4_2_7/tests/domain_usage.csv'


def read_csv_file(filename: str) -> List[List[str]]:
    """Reads a CSV file and returns its content as a list of rows.

    Args:
        filename (str): The path to the CSV file.

    Returns:
        List[List[str]]: The content of the CSV file.
    """
    with open(filename, 'r', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        return [row for row in reader]


def write_to_csv_file(data: List[List[Any]], filename: str, columns: List[str] = []) -> None:
    """Writes a list of rows to a CSV file.

    Args:
        data (List[List[Any]]): The data to write.
        filename (str): The path to the CSV file.
        columns (List[str], optional): The column headers. Defaults to [].
    """
    with open(filename, 'w', encoding='utf-8', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        if columns:
            writer.writerow(columns)
        for row in data:
            writer.writerow(row)


def count_domain_occurrences(data: List[List[str]]) -> Dict[str, int]:
    """Counts the occurrences of each domain in the data.

    Args:
        data (List[List[str]]): The CSV data.

    Returns:
        Dict[str, int]: A dictionary with domain counts.
    """
    domains_counter = {}
    for row in data[1:]:
        login, domain = row[2].split('@')
        if domain in domains_counter:
            domains_counter[domain] += 1
        else:
            domains_counter[domain] = 1
    return domains_counter


def convert_dict_to_list_of_lists(any_dict: Dict[Any, Any]) -> List[List[Any]]:
    """Converts a dictionary to a list of lists.

    Args:
        any_dict (Dict[Any, Any]): The dictionary to convert.

    Returns:
        List[List[Any]]: The resulting list of lists.
    """
    return [[key, value] for key, value in any_dict.items()]


data = read_csv_file(FILE_TO_READ)
domain_occurrences = convert_dict_to_list_of_lists(count_domain_occurrences(data))
data_to_write = sorted(domain_occurrences, key=lambda x: [x[1], x[0]])

header_columns = ['domain', 'count']

# Write the sorted data to the output file
write_to_csv_file(data_to_write, FILE_TO_WRITE, columns=header_columns)
