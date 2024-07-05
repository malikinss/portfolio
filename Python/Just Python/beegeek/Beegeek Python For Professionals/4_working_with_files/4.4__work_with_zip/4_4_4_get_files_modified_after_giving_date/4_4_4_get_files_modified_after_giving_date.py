
'''
TODO:
        You have access to the workbook.zip archive, which contains various
        folders and files.

        Write a program that prints the names of files in this archive that
        were created or modified later than 2021-11-30 14:22:00.

        File names should be in lexicographic order, each on a separate line.

NOTE:
        If the file is in a folder, only the name should be printed without
        the path.

        The initial part of the response looks like this:
            countries.json
            data_sample.csv
            ...
'''
from zipfile import ZipFile, ZipInfo
from typing import List
from datetime import datetime


def tuple_to_datetime_tuple(date_tuple: tuple) -> datetime:
    """
    Convert a tuple representing date and time to a datetime object.

    Args:
        date_tuple (tuple):
            A tuple of (year, month, day, hour, minute, second).

    Returns:
        datetime: A datetime object representing the given date and time.
    """
    return datetime(*date_tuple)


def is_datetime_after(input_datetime: datetime,
                      target_datetime: datetime) -> bool:
    """
    Check if input_datetime is after target_datetime.

    Args:
        input_datetime (datetime): The datetime to check.
        target_datetime (datetime): The datetime to compare against.

    Returns:
        bool: True if input_datetime is after target_datetime, False otherwise.
    """
    return input_datetime > target_datetime


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


def get_filename_from_zipinfo(file_info: ZipInfo) -> str:
    """
    Extract the filename from the ZipInfo object.

    Args:
        file_info (ZipInfo): The ZipInfo object.

    Returns:
        str: The filename without the path.
    """
    return file_info.filename.split('/')[-1]


def get_files_modified_after_giving_date(files: List[ZipInfo],
                                         giving_date: datetime) -> List[str]:
    """
    Get filenames of files modified after a given datetime from a list
    of ZipInfo objects.

    Args:
        files (List[ZipInfo]): A list of ZipInfo objects representing files in
        a zip archive.
        giving_date (datetime): The datetime after which files are
        considered modified.

    Returns:
        List[str]: A list of filenames (without path) modified after the
        giving_date, sorted lexicographically.
    """
    new_files = []

    for file_info in files:
        if not file_info.is_dir():
            filename = get_filename_from_zipinfo(file_info)
            dtime_obj = tuple_to_datetime_tuple(file_info.date_time)

            if is_datetime_after(dtime_obj, giving_date):
                new_files.append(filename)

    return sorted(new_files)


if __name__ == '__main__':
    filename = '4_4_4/tests/workbook.zip'
    files_info = get_zip_file_info(filename)

    target_datetime = datetime(2021, 11, 30, 14, 22, 0)

    result = get_files_modified_after_giving_date(files_info, target_datetime)
    print(*result, sep='\n')
