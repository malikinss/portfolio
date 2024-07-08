'''
TODO:
        You have a list of files containing the names of different files.

        Complete the code below so that it prints all the file extensions
        present in the list files, indicating for each the number of files
        with that extension.

        The extensions must be in lexicographic order, each on a separate line,
        in the following format:
            <extension>: <number of files>
'''
from collections import Counter
from typing import List


def get_extension_list(files: List[str]) -> List[str]:
    """
    Extracts and returns the list of file extensions from the given list of
    file names.

    Args:
        files (List[str]): A list of file names.

    Returns:
        List[str]: A sorted list of file extensions.
    """
    extensions_list = []
    for file in files:
        # Extract the file extension
        _, extension = file.split('.')
        extensions_list.append(extension)
    return sorted(extensions_list)


def count_extensions(files: List[str]) -> Counter:
    """
    Counts the occurrences of each file extension in the given list of
    file names.

    Args:
        files (List[str]): A list of file names.

    Returns:
        Counter: A Counter object with the count of each file extension.
    """
    extensions = get_extension_list(files)
    # Count the number of occurrences of each extension
    extensions_cnt = Counter(extensions)
    return extensions_cnt


def display_extension_counts(extension_counts: Counter) -> None:
    """
    Displays the count of each file extension in the specified format.

    Args:
        extension_counts (Counter): A Counter object with the count of each
        file extension.
    """
    for extension, amount in extension_counts.items():
        print(f'{extension}: {amount}')


files = ['emoji_smile.jpeg', 'city-of-the-sun.mp3', 'dhook_hw.json',
         'sample.xml', 'teamspeak3.exe', 'project_module3.py',
         'math_lesson3.mp4', 'old_memories.mp4', 'spiritfarer.exe',
         'backups.json', 'python_for_beg1.mp4', 'emoji_angry.jpeg',
         'exam_results.csv', 'project_main.py', 'classes.csv',
         'plants.xml', 'cant-help-myself.mp3', 'microsoft_edge.exe',
         'steam.exe', 'math_lesson4.mp4', 'city.jpeg',
         'bad-disease.mp3', 'beauty.jpeg', 'hollow_knight_silksong.exe',
         'whatsapp.exe', 'photoshop.exe', 'telegram.exe',
         'yandex_browser.exe', 'math_lesson7.mp4', 'students.csv',
         'emojis.zip', '7z.zip', 'bones.mp3', 'python3.zip',
         'dhook_lsns.json', 'carl_backups.json', 'forest.jpeg',
         'python_for_pro8.mp4', 'yandexdisc.exe', 'but-you.mp3',
         'project_module1.py', 'nothing.xml', 'flowers.jpeg',
         'grades.csv', 'nvidia_gf.exe', 'small_txt.zip',
         'project_module2.py', 'tab.csv', 'note.xml',
         'sony_vegas11.exe', 'friends.jpeg', 'data.pkl']

# Get the counts of each file extension
extensions = count_extensions(files)
# Display the extension counts
display_extension_counts(extensions)
