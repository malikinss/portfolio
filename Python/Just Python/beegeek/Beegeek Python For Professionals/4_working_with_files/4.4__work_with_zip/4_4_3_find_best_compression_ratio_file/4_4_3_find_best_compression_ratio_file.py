
'''
TODO:
        You have access to the workbook.zip archive, which contains various
        folders and files.

        Write a program that outputs the name of the file from this archive
        that has the best compression ratio.

NOTE:
        If the file is in a folder, only the name should be output without
        the path.

        It is guaranteed that only one file in the original archive has
        the best compression ratio.

        The compression ratio of a file is characterized by the coefficient 𝐾,
        defined as the ratio of the compressed file size 𝑉𝑐 to the original
        file size 𝑉𝑜, expressed as a percentage.
'''
from zipfile import ZipFile, ZipInfo
from typing import List, Dict


def get_zip_file_info_list(file_path: str) -> List[ZipInfo]:
    """
    Get a list of ZipInfo objects for the files in the given zip archive.

    Args:
        file_path (str): The path to the zip archive.

    Returns:
        List[ZipInfo]: A list of ZipInfo objects.
    """
    with ZipFile(file_path) as zip_file:
        return zip_file.infolist()


def calculate_compression_ratio_percentage(original_size: int,
                                           compressed_size: int) -> float:
    """
    Calculate the compression ratio of a file as a percentage.

    Args:
        original_size (int): The original size of the file.
        compressed_size (int): The compressed size of the file.

    Returns:
        float: The compression ratio as a percentage.
    """
    return (compressed_size / original_size) * 100


def extract_filename(file_info: ZipInfo) -> str:
    """
    Extract the filename from the ZipInfo object.

    Args:
        file_info (ZipInfo): The ZipInfo object.

    Returns:
        str: The filename without the path.
    """
    filename = file_info.filename
    if '/' in filename:
        return filename.split('/')[-1]
    return filename


def calculate_compression_ratios(files_info: List[ZipInfo]) -> Dict[str, float]:
    """
    Calculate the compression ratios for each file in the zip archive.

    Args:
        files_info (List[ZipInfo]): A list of ZipInfo objects.

    Returns:
        Dict[str, float]: A dictionary with filenames as keys and their
        compression ratios as values.
    """
    files_compress_ratios = {}
    for file_info in files_info:
        original_size = file_info.file_size
        compressed_size = file_info.compress_size

        if original_size != 0 and not file_info.is_dir():
            filename = extract_filename(file_info)
            ratio = calculate_compression_ratio_percentage(original_size,
                                                           compressed_size)
            files_compress_ratios[filename] = ratio

    return files_compress_ratios


def find_best_compression_ratio_file(compression_ratios: Dict[str, float]) -> str:
    """
    Find the filename with the best (minimum) compression ratio.

    Args:
        compression_ratios (Dict[str, float]): A dictionary with filenames
        and their compression ratios.

    Returns:
        str: The filename with the best compression ratio.
    """
    return min(compression_ratios, key=compression_ratios.get)


if __name__ == '__main__':
    filename = '4_4_3/tests/workbook.zip'
    files_info = get_zip_file_info_list(filename)
    files_compression_ratios = calculate_compression_ratios(files_info)

    result = find_best_compression_ratio_file(files_compression_ratios)
    print(result)
