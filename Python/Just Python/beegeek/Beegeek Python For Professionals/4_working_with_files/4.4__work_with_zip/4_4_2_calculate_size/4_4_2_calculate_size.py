
'''
TODO:
        The workbook.zip archive is available, containing various folders
        and files.

        Write a program that outputs the total size of the files in this
        archive in compressed and uncompressed form in bytes, in the
        following format:
            Size of original files: <size before compression> bytes
            Size of compressed files: <size after compression> bytes
'''
from zipfile import ZipFile, ZipInfo
from typing import List, Callable


def get_zip_file_info(file_path: str) -> List[ZipInfo]:
    '''
    Get a list of ZipInfo objects for the files in the given zip archive.'''
    with ZipFile(file_path) as zip_file:
        return zip_file.infolist()


def calculate_size(files_info: List[ZipInfo],
                   size_getter: Callable[[ZipInfo], int]) -> int:
    '''
    Calculate the total size of the files in the zip archive using the
    provided size getter function.
    '''
    return sum(size_getter(file_info) for file_info in files_info if not file_info.is_dir())


def calculate_uncompressed_size(files_info: List[ZipInfo]) -> int:
    '''
    Calculate the total uncompressed size of the files in the zip archive.
    '''
    return calculate_size(files_info, lambda f: f.file_size)


def calculate_compressed_size(files_info: List[ZipInfo]) -> int:
    '''
    Calculate the total compressed size of the files in the zip archive.
    '''
    return calculate_size(files_info, lambda f: f.compress_size)


def print_sizes(uncompressed_size: int, compressed_size: int) -> None:
    '''
    Print the uncompressed and compressed sizes of the files.
    '''
    print(f'Объем исходных файлов: {uncompressed_size} байт(а)')
    print(f'Объем сжатых файлов: {compressed_size} байт(а)')


if __name__ == '__main__':
    # Define the path to the zip file
    filename = '4_4_2/tests/workbook.zip'

    # Get file information from the zip archive
    files_info = get_zip_file_info(filename)

    # Calculate uncompressed and compressed sizes
    uncompressed_size = calculate_uncompressed_size(files_info)
    compressed_size = calculate_compressed_size(files_info)

    # Display the results
    print_sizes(uncompressed_size, compressed_size)
