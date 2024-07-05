'''
TODO:
    You have access to a set of different files, the names of which are
    presented in the file_names list.

    Complete the code below so that it creates an archive files.zip and
    adds all the files from this list to it.

NOTE:
    Assume that the files from the file_names list are in the
    program folder.
'''
from zipfile import ZipFile
from typing import List


def write_to_zip(files: List[str]) -> None:
    """
    Creates a zip archive named 'files.zip' and adds the given files to it.

    Parameters:
    files (List[str]): A list of filenames to be added to the zip archive.
    """
    with ZipFile('files.zip', 'w') as zip_file:
        for file in files:
            zip_file.write(file)


file_names = [
    'how to prove.pdf', 'fipi_demo_2022.pdf',
    'Hollow Knight Silksong.exe', 'code.jpeg',
    'stepik.png', 'readme.txt', 'shopping_list.txt',
    'Alexandra Savior – Crying All the Time.mp3',
    'homework.py', 'test.py'
]

write_to_zip(file_names)
