'''
TODO:
        You have access to the data.zip archive, which contains various
        folders and files.

        Among them are several JSON files, each containing information about
        a football player:
            {
            "first_name": "Gary",
            "last_name": "Cahill",
            "team": "Chelsea",
            "position": "Defender"
            }

        A football player has the following attributes:
            first_name — first name
            last_name — last name
            team — name of the football club
            position — playing position

        Write a program that processes only these JSON files and outputs the
        first and last names of football players who play
        for Arsenal Football Club.

        The players should be listed in lexicographical order of their names,
        and if there is a match, in lexicographical order of their last names,
        each on a separate line.

NOTE:
        Please note that the presence of the .json extension on a file
        doesn't guarantee that it is a valid text file in JSON format.

        To determine if a file is a valid JSON text file, use the try-except
        construct and the is_correct_json() function from the previous lesson.

        The initial part of the response looks like this:
            Alex Iwobi
            Alexis Sanchez
            ...
'''
import json
from zipfile import ZipFile
from typing import List, Tuple, Dict, Any


def is_file(file_info) -> bool:
    """
    Check if the file_info corresponds to a file and not a directory.
    """
    return not file_info.is_dir()


def get_full_name(data: Dict[str, Any]) -> Tuple[str, str]:
    """
    Extract the full name (first and last) from the player data.
    """
    return data.get('first_name', ''), data.get('last_name', '')


def sort_player_names(names: List[Tuple[str, str]]) -> List[Tuple[str, str]]:
    """
    Sort player names first by first name, then by last name.
    """
    return sorted(names, key=lambda name: (name[0], name[1]))


def get_specific_club_players(zip_file_path: str,
                              club_name: str) -> List[Tuple[str, str]]:
    """
    Extract and sort names of players from the specified club within
    a ZIP file.
    """
    arsenal_players_names = []

    with ZipFile(zip_file_path) as zfile:
        for file_info in zfile.infolist():
            current_filename = file_info.filename

            if is_file(file_info) and current_filename.endswith('.json'):
                with zfile.open(current_filename, 'r') as json_file:
                    try:
                        data = json.load(json_file)

                        if data.get('team') == club_name:
                            arsenal_players_names.append(get_full_name(data))
                    except (ValueError, KeyError):
                        pass

    return sort_player_names(arsenal_players_names)


def display_players(players: List[Tuple[str, str]]) -> None:
    """
    Print the full names of players.
    """
    for first_name, last_name in players:
        print(f"{first_name} {last_name}")


# Define the path to the ZIP file
directory = '4_4_9/tests'
zip_file_name = 'data.zip'
zip_file_path = f'{directory}/{zip_file_name}'

# Get and display players from Arsenal
arsenal_players = get_specific_club_players(zip_file_path, 'Arsenal')
display_players(arsenal_players)
