'''
TODO:
        Implement a function csv_columns() that takes one argument:
            filename — the name of the csv file, for example, data.csv

        The function should return a dictionary in which the key is the name
        of the file column filename, and the value is a list of elements of
        this column.

NOTE:
        It is guaranteed that the file passed to the function is delimited by
        a comma, and quotation marks are not used.

        It is guaranteed that the first line of the file passed to the
        function contains the names of the columns.

        For example, if the file exam.csv were:
            name,grade
            Timur,5
            Arthur,4
            Anri,5

        then the following call to the csv_columns() function:
            csv_columns('exam.csv')
        should return:
            {'name': ['Timur', 'Arthur', 'Anri'], 'grade': ['5', '4', '5']}

        The keys in the dictionary, as well as the elements in the lists, must
        be in their original order.
'''
import csv
from typing import List, Dict


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


def create_empty_dict_with_headers(column_headers: List[str]) -> Dict[str, List[str]]:
    """Creates an empty dictionary with headers as keys.

    Args:
        column_headers (List[str]): The column headers.

    Returns:
        Dict[str, List[str]]: An empty dictionary with column headers as keys.
    """
    return {header: [] for header in column_headers}


def parse_csv_data(csv_data: List[List[str]]) -> Dict[str, List[str]]:
    """Parses CSV data into a dictionary.

    Args:
        csv_data (List[List[str]]): The CSV data.

    Returns:
        Dict[str, List[str]]: The parsed data as a dictionary.
    """
    headers = csv_data[0]
    data_dict = create_empty_dict_with_headers(headers)
    for row in csv_data[1:]:
        for i, value in enumerate(row):
            data_dict[headers[i]].append(value)
    return data_dict


def csv_columns(filename: str) -> Dict[str, List[str]]:
    """Reads a CSV file and returns a dictionary with column data.

    Args:
        filename (str): The name of the CSV file.

    Returns:
        Dict[str, List[str]]: A dictionary with column names as keys and
        column data as values.
    """
    csv_data = read_csv_file(filename)
    return parse_csv_data(csv_data)
