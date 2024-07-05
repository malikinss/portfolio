'''
TODO:
        The archive workbook.zip is available, containing various folders
        and files.

        Write a program that outputs a single number — the number of files
        in this archive.

NOTE:
        Note that a folder is not considered a file.
'''
from zipfile import ZipFile


def count_files_in_zip(file_path: str) -> int:
    """
    Count the number of files (not folders) in a ZIP archive.

    Args:
        file_path (str): Path to the ZIP archive file.

    Returns:
        int: Number of files in the ZIP archive.
    """
    with ZipFile(file_path) as zip_file:
        file_count = sum(1 for file_info in zip_file.infolist() if not file_info.is_dir())

    return file_count


if __name__ == '__main__':
    filename = '4_4_1/tests/workbook.zip'
    files_num = count_files_in_zip(filename)
    print(files_num)
