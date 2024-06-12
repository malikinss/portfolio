'''
TODO:
        Let's consider the following text fragment:
            ball,color,purple
            ball,size,4
            ball,notes,it's round
            cup,color,blue
            cup,size,1
            cup,notes,none

        Each line of this fragment contains three values separated by commas:
            the name of the object
            the property of this object
            the value of the property.

        For example, the first line contains the object ball, which has the
        property color, the value of which is purple.

        The object ball also has the properties size and notes, which have the
        values 4 and it's round, respectively.

        In addition to the object ball, there is an object cup, which has the
        same properties and in the same quantity.

        We will give these objects a common name object and group the lines of
        this text fragment by the first column:
            object,color,size,notes
            ball,purple,4,it's round
            cup,blue,1,none

        We received a record in the usual CSV format, in which the first
        column indicates the name of the object, and the following ones
        indicate the values of the corresponding properties of this object.

        Implement the condense_csv() function, which takes two arguments in
        the following format:
            filename — the name of the csv file, for example, data.csv;

        the format of the file contents is similar to the format of the text
        fragment considered in the problem statement: each line of the file
        contains three values separated by commas, namely the name of the
        object, the property of this object, the value of the property;

        all objects have equal properties and in equal quantities

            id_name — a common name for objects

        The function should convert the contents of the file to the usual CSV
        format, grouping the lines by the first column and naming the first
        column id_name.

        The function should write the result to the condensed.csv file.

NOTE:
        For example, if the data.csv file was:
            01,Title,Ran So Hard the Sun Went Down
            02,Title,Honky Tonk Heroes (Like Me)

        then calling the condense_csv() function:
            condense_csv('data.csv', id_name='ID')

        would create a condensed.csv file with the following contents:
            ID,Title
            01,Ran So Hard the Sun Went Down
            02,Honky Tonk Heroes (Like Me)

        The file passed to the csv function is guaranteed to be
        comma-separated, and no quotation marks are used.

        When opening the file, explicitly specify UTF-8 encoding.
'''
import csv
from typing import List, Dict

FILE_TO_READ = 'data.csv'
FILE_TO_WRITE = '4_2_11/tests/condensed.csv'


def read_csv_file(filename: str,
                  delimiter: str = ',') -> List[List[str]]:
    """
    Reads a CSV file and returns its content as a list of rows.

    Args:
        filename (str): The path to the CSV file.
        delimiter (str): The delimiter used in the CSV file.

    Returns:
        List[List[str]]: The content of the CSV file as a list of rows.
    """
    with open(filename, 'r', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file, delimiter=delimiter)
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


def extract_ids(csv_data: List[List[str]]) -> List[str]:
    """
    Extracts unique IDs from the CSV data.

    Args:
        csv_data (List[List[str]]): The CSV data as a list of rows.

    Returns:
        List[str]: A list of unique IDs.
    """
    ids = []
    for row in csv_data:
        if row[0] not in ids:
            ids.append(row[0])
    return ids


def extract_headers(csv_data: List[List[str]],
                    id_column_name: str) -> List[str]:
    """
    Extracts headers from the CSV data.

    Args:
        csv_data (List[List[str]]): The CSV data as a list of rows.
        id_column_name (str): The name to use for the ID column.

    Returns:
        List[str]: A list of headers.
    """
    headers = [id_column_name]
    for row in csv_data:
        if row[1] not in headers:
            headers.append(row[1])
    return headers


def create_records(csv_data: List[List[str]],
                   headers: List[str],
                   ids: List[str]) -> List[Dict[str, str]]:
    """Creates a list of records from the CSV data.

    Args:
        csv_data (List[List[str]]): The CSV data as a list of rows.
        headers (List[str]): The list of headers.
        ids (List[str]): The list of unique IDs.

    Returns:
        List[Dict[str, str]]: A list of records as dictionaries.
    """
    records = {}
    id_name = headers[0]
    for id in ids:
        records[id] = {id_name: id}

        for header in headers[1:]:
            for row in csv_data:
                if row[0] == id and row[1] == header:
                    records[id][header] = row[2]

    return list(records.values())


def condense_csv(filename: str, id_name: str) -> None:
    """
    Condenses a CSV file into a summarized format and writes the result to a
    new file.

    Args:
        filename (str): The path to the input CSV file.
        id_name (str): The name to use for the ID column in the output CSV
        file.
    """
    csv_data = read_csv_file(filename)
    ids = extract_ids(csv_data)
    headers = extract_headers(csv_data, id_name)
    records = create_records(csv_data, headers, ids)
    write_csv(records, FILE_TO_WRITE, headers)


condense_csv(filename=FILE_TO_READ, id_name='ID')
