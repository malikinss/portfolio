
'''
TODO:
        You have access to the workbook.zip archive, which contains various
        folders and files.

        Write a program that outputs the names of all files in this archive in
        lexicographic order, indicating for each its modification date, as
        well as the size before and after compression, in the following format:
            <file name>
            File modification date: <modification date>
            Size of the original file: <size before compression> bytes
            Size of the compressed file: <size after compression> bytes

        There must be an empty line between the data about the two files.

NOTE:
        If the file is in a folder, only the name should be output without
        the path.

        The initial part of the response looks like this (use two spaces
        for indentation):
            Alexandra Savior - Crying All the Time.mp3
            File modification date: 2021-11-30 13:27:02
            Original file size: 5057559 bytes
            Compressed file size: 5051745 bytes

            Hollow Knight Silksong.exe
            File modification date: 2013-08-22 08:20:06
            Original file size: 805992 bytes
            Compressed file size: 494930 bytes
            ...
'''
from zipfile import ZipFile, ZipInfo
from typing import List, Dict
from datetime import datetime


def get_zip_file_info(file_path: str) -> List[ZipInfo]:
    """
    Get a list of ZipInfo objects for the files in the given zip archive.

    Args:
        file_path (str): The path to the zip archive.

    Returns:
        List[ZipInfo]: A list of ZipInfo objects.
    """
    with ZipFile(file_path) as zip_file:
        return zip_file.infolist()


def get_filename_from_zip_info(file_info: ZipInfo) -> str:
    """
    Extract the filename from the ZipInfo object.

    Args:
        file_info (ZipInfo): The ZipInfo object.

    Returns:
        str: The filename without the path.
    """
    filename = file_info.filename
    return filename.split('/')[-1]


def datetime_tuple_to_str(date_tuple: tuple) -> str:
    """
    Convert a date time tuple to a string in the format 'YYYY-MM-DD HH:MM:SS'.

    Args:
        date_tuple (tuple): The date time tuple.

    Returns:
        str: The formatted date time string.
    """
    return datetime(*date_tuple).strftime('%Y-%m-%d %H:%M:%S')


def get_formatted_info(files: List[ZipInfo]) -> Dict[str, List[str]]:
    """
    Extract and format information from a list of ZipInfo objects.

    Args:
        files (List[ZipInfo]): A list of ZipInfo objects.

    Returns:
        Dict[str, List[str]]: A dictionary with filenames as keys and lists of
        file attributes as values.
    """
    formatted_info = {}

    for file in files:
        if not file.is_dir():
            name = get_filename_from_zip_info(file)
            date_time = datetime_tuple_to_str(file.date_time)
            original_size = file.file_size
            compressed_size = file.compress_size

            formatted_info[name] = [date_time, original_size, compressed_size]

    return dict(sorted(formatted_info.items()))


def display_formatted_info(formatted_info: Dict[str, List[str]]) -> None:
    """
    Display formatted file information.

    Args:
        formatted_info (Dict[str, List[str]]): The formatted file information.
    """
    prefixes = ['Дата модификации файла',
                'Объем исходного файла',
                'Объем сжатого файла']

    for name, value in formatted_info.items():
        print(name)

        for i in range(len(value)):
            main_part = f'  {prefixes[i]}: {value[i]}'

            if i == 0:
                print(main_part)
            else:
                print(f'{main_part} байт(а)')

        print()  # Add an empty line between file entries


if __name__ == '__main__':
    filename = '4_4_5/tests/workbook.zip'
    files_info = get_zip_file_info(filename)
    formatted_info = get_formatted_info(files_info)
    display_formatted_info(formatted_info)
