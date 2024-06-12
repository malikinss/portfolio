'''
TODO:
        You have access to the student_counts.csv file, which contains data on
        the number of students in a certain educational institution for the
        period 2000 - 2021

        The first column contains the year, the following columns contain the
        class and the number of students in this class in this year:
            year,5-B,3-B,8-A,2-G,7-B,1-B,3-G,3-A,2-B,6-B,6-A,8-B,8-G,11-A,2-A,7-A,5-A,2-B,10-A,11-B,8-B,4-A,7-B,3-B,1-A,9-A,11-B
            2000,19,15,18,29,19,17,26,29,28,30,26,27,27,22,29,19,27,20,16,18,15,27,19,29,22,20,23
            2001,21,30,22,19,26,20,24,27,20,30,24,30,29,21,20,19,29,27,23,25,30,30,23,22,22,18,22
            ...

        Write a program that writes this table to the file
        sorted_student_counts.csv, arranging all columns in ascending order of
        classes, if the classes match - in ascending order of letters.

NOTE:
        Each class contains a number and a letter and is written in the
        following format:
            <class number>-<class letter>

        The separator in the student_counts.csv file is a comma, and quotation
        marks are not used.

        The initial part of the sorted_student_counts.csv file looks like this:
            year,1-A,1-B,2-A,2-B,...
            2000,22,17,29,20,...
            2001,22,20,20,27,...
            ...

        When opening the file, use an explicit UTF-8 encoding.
'''
import csv
from typing import List, Dict, Tuple

FILE_TO_READ = '4_2_12/tests/student_counts.csv'
FILE_TO_WRITE = '4_2_12/tests/sorted_student_counts.csv'


def read_csv(filename: str,
             delimiter: str = ',') -> List[Dict[str, str]]:
    """
    Reads a CSV file and returns its content as a list of dictionaries.

    Args:
        filename (str): The path to the CSV file.
        delimiter (str): The delimiter used in the CSV file.

    Returns:
        List[Dict[str, str]]: The content of the CSV file as a list of
        dictionaries.
    """
    with open(filename, 'r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=delimiter)
        return [row for row in reader]


def write_csv(data: List[Dict[str, str]],
              filename: str,
              columns: List[str],
              delimiter: str = ',') -> None:
    """
    Writes data to a CSV file.

    Args:
        data (List[Dict[str, str]]): The data to write, as a list of
        dictionaries.
        filename (str): The path to the output CSV file.
        columns (List[str]): The column names to use in the CSV file.
        delimiter (str): The delimiter to use in the CSV file.
    """
    with open(filename, 'w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=columns, delimiter=delimiter)
        writer.writeheader()
        writer.writerows(data)


def sort_headers(headers: List[str]) -> List[str]:
    """
    Sorts the headers of the CSV file in the specified format.

    Args:
        headers (List[str]): The headers to sort.

    Returns:
        List[str]: The sorted headers.
    """
    classes_under_10 = []
    classes_above_and_include_10 = []
    result_headers = []

    for header in headers:
        if len(header) == 3:
            classes_under_10.append(header)
        elif len(header) == 4 and header != 'year':
            classes_above_and_include_10.append(header)
        elif header == 'year':
            result_headers.append(header)

    result_headers += sorted(classes_under_10)
    result_headers += sorted(classes_above_and_include_10)

    return result_headers


def extract_headers(data: List[Dict[str, str]]) -> List[str]:
    """
    Extracts headers from the data.

    Args:
        data (List[Dict[str, str]]): The data from which to extract headers.

    Returns:
        List[str]: The extracted headers.
    """
    return list(data[0].keys())


def sort_rows(rows: List[Dict[str, str]],
              sorted_headers: List[str]) -> List[Dict[str, str]]:
    """
    Sorts the rows according to the sorted headers.

    Args:
        rows (List[Dict[str, str]]): The rows to sort.
        sorted_headers (List[str]): The sorted headers.

    Returns:
        List[Dict[str, str]]: The sorted rows.
    """
    sorted_rows = []

    for row in rows:
        sorted_row = {header: row[header] for header in sorted_headers}
        sorted_rows.append(sorted_row)

    return sorted_rows


def sort_students_per_year_and_class(filename: str) -> Tuple[List[Dict[str, str]], List[str]]:
    """
    Sorts the student counts per year and class.

    Args:
        filename (str): The path to the CSV file.

    Returns:
        Tuple[List[Dict[str, str]], List[str]]: A tuple containing sorted rows
        and headers.
    """
    data = read_csv(filename)
    headers = extract_headers(data)
    sorted_headers = sort_headers(headers)
    sorted_rows = sort_rows(data, sorted_headers)

    return sorted_rows, sorted_headers


sorted_data, sorted_headers = sort_students_per_year_and_class(FILE_TO_READ)
write_csv(sorted_data, FILE_TO_WRITE, sorted_headers)
