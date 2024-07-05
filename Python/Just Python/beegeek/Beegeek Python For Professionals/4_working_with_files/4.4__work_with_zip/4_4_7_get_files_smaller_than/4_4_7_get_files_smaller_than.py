'''
TODO:
        You have access to a set of different files, the names of which are
        presented in the file_names list.

        You can also access the files.zip archive.

        Complete the code below so that it adds to the files.zip archive only
        those files from the file_names list whose size doesn't
        exceed 100 bytes.

NOTE:
        You can get the file size in bytes using the getsize() function from
        the os.path module.

        This function takes the path to the file as an argument and returns
        the size of the specified file in bytes.

        For example, you can calculate the size of the files.zip archive in
        bytes and save it in the size variable as follows:
            import os.path
            size = os.path.getsize('files.zip')

        You can also calculate the file size in bytes manually, without
        resorting to third-party modules.
        Think about it 😉.

        Assume that the files from the file_names list and the files.zip
        archive are in the program folder.
'''
from zipfile import ZipFile
from typing import List
import os


def write_to_zip(files: List[str]) -> None:
    """
    Creates a zip archive named 'files.zip' and adds the given files to it.

    Parameters:
    files (List[str]): A list of filenames to be added to the zip archive.
    """
    with ZipFile('files.zip', 'w') as zip_file:
        for file in files:
            zip_file.write(file, arcname=os.path.basename(file))


def get_file_size_in_bytes(file_path: str) -> int:
    """
    Returns the size of the specified file in bytes.

    Parameters:
    file_path (str): The path to the file.

    Returns:
    int: The size of the file in bytes.
    """
    return os.path.getsize(file_path)


def get_files_smaller_than(files: List[str], max_size: int) -> List[str]:
    """
    Returns a list of files whose size is less than the given max_size.

    Parameters:
    files (List[str]): A list of filenames.
    max_size (int): The maximum file size in bytes.

    Returns:
    List[str]: A list of filenames that are smaller than max_size.
    """
    return [file for file in files if get_file_size_in_bytes(file) < max_size]


file_names = ['how to prove.pdf', 'fipi_demo_2022.pdf',
              'Hollow Knight Silksong.exe', 'code.jpeg',
              'stepik.png', 'readme.txt', 'shopping_list.txt',
              'Alexandra Savior – Crying All the Time.mp3',
              'homework.py', 'test.py']

new_file_names = get_files_smaller_than(file_names, 101)
write_to_zip(new_file_names)
