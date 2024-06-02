'''
TODO:
        You have access to the deniro.csv file, each column of which contains
        either only numbers or string values:
            Machete,2010,72
            Marvin's Room,1996,80
            Raging Bull,1980,97
            ...

        Write a program that sorts the contents of this file by the specified
        column.

        Moreover, the data should be sorted in ascending order of numbers if
        the column contains numbers, and in lexicographic order of words if
        the column contains words.


        Input:
            The program receives a natural number as input — the column number
            of the deniro.csv file.

        Output:
            The program should sort the contents of the deniro.csv file by the
            entered column and output the result in the original format.

NOTE:
        Column numbering starts with one.
        For example, if the deniro.csv file was:
            red,4
            blue,3
            green,28
            purple,1
        and it needed to be sorted by the second column (in ascending
        numerical order), then the program should output:
            purple,1
            blue,3
            red,4
            green,28

        If any two rows have the same values ​​in the columns, then their
        original order should be preserved.

        The separator in the deniro.csv file is a comma, and quotation marks
        are not used.
'''
import csv
from typing import List


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


def print_table(table: List[List[str]]) -> None:
    """Prints the content of a table row by row.

    Args:
        table (List[List[str]]): The table to be printed.
    """
    for row in table:
        print(','.join(row))


def sort_table_by_column(table: List[List[str]], column_index: int) -> List[List[str]]:
    """Sorts the table by a specified column.

    Args:
        table (List[List[str]]): The table to be sorted.
        column_index (int): The index of the column to sort by.

    Returns:
        List[List[str]]: The sorted table.
    """
    # Check if column contains numeric values
    try:
        return sorted(table, key=lambda x: float(x[column_index]))
    except ValueError:
        return sorted(table, key=lambda x: x[column_index])


# Read the column index to sort by (input is 1-based, so convert to 0-based)
column_index = int(input("Enter column number to sort by: ")) - 1

# Path to the CSV file
filename = 'deniro.csv'

# Read the CSV file
table = read_csv_file(filename)

# Sort the table by the specified column
sorted_table = sort_table_by_column(table, column_index)

# Print the sorted table
print_table(sorted_table)
