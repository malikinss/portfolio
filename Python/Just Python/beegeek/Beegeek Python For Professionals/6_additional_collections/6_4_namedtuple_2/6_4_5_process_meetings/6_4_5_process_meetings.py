'''
TODO:
        Timur has many friends from other cities or countries who often come
        to visit him to see each other and have fun.
        In order not to forget about a single meeting, Timur writes down the
        names and surnames of his friends in a csv file, additionally
        indicating the date and time of the meeting for each.
        You can access this file, called meetings.csv, in which:
            the first column contains the surname
            the second - the name
            the third - the date in the DD.MM.YYYY format
            the fourth - the time in the HH:MM format:

            surname, name, meeting_date, meeting_time
            Kharisov, Artur, 07/15/2022, 05:00 PM
            Geor, Gagiev, 12/14/2022, 06:00 PM
            ...

        Write a program that displays the names and surnames of Timur's
        friends, having previously sorted them by the date and time of the
        meeting from the earliest to the latest.
        Last names and first names must be placed on a separate line.

NOTE:
        The initial part of the response looks like this:
            Gudtsev Taimuraz
            Kharisov Artur
            Baziyev German
            ...

        It is guaranteed that no two meetings have the same date and time at
        the same time.

        The separator in the meetings.csv file is a comma, and quotation marks
        are not used.

        When opening the file, use an explicit UTF-8 encoding.
'''
import csv
from typing import List, Dict
from collections import namedtuple
from datetime import datetime


Meeting = namedtuple('Meeting', 'surname name meeting_date meeting_time')


def read_csv(filename: str, delimiter: str = ',') -> List[Dict[str, str]]:
    """
    Reads a CSV file and returns its content as a list of dictionaries.

    Args:
        filename (str): The path to the CSV file.
        delimiter (str): The delimiter used in the CSV file.

    Returns:
        List[Dict[str, str]]: The content of the CSV file as a list
        of dictionaries.
    """
    with open(filename, 'r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=delimiter)

        return [row for row in reader]


def convert_meeting_to_datetime(meeting: Meeting) -> datetime:
    """
    Converts the date and time strings of a meeting into a datetime object.

    Args:
        meeting (Meeting): A namedtuple representing a meeting.

    Returns:
        datetime: A datetime object representing the combined date and time.
    """
    str_date = f'{meeting.meeting_date} {meeting.meeting_time}'
    time_format = '%d.%m.%Y %H:%M'

    return datetime.strptime(str_date, time_format)


def get_full_name(meeting: Meeting) -> str:
    """
    Returns the full name (surname and name) from a meeting.

    Args:
        meeting (Meeting): A namedtuple representing a meeting.

    Returns:
        str: The full name formatted as 'surname name'.
    """
    return f'{meeting.surname} {meeting.name}'


def create_sorted_meetings(data: List[Dict[str, str]]) -> List[Meeting]:
    """
    Creates a list of Meeting namedtuples from a list of dictionaries and
    sorts them by datetime.

    Args:
        data (List[Dict[str, str]]): The list of dictionaries containing
        meeting data.

    Returns:
        List[Meeting]: A sorted list of Meeting namedtuples.
    """
    meetings = [Meeting(**record) for record in data]
    meetings.sort(key=convert_meeting_to_datetime)

    return meetings


def print_meetings(meetings: List[Meeting]) -> None:
    """
    Prints the full names of meetings.

    Args:
        meetings (List[Meeting]): The list of meetings to print.
    """
    for meet in meetings:
        print(get_full_name(meet))


def process_meetings(csv_path: str) -> None:
    """
    Reads, processes, and prints meeting information from a CSV file.

    Args:
        csv_path (str): The path to the CSV file.
    """
    data = read_csv(csv_path)
    meetings = create_sorted_meetings(data)
    print_meetings(meetings)


if __name__ == '__main__':
    csv_path = './6_4_5_process_meetings/tests/meetings.csv'
    process_meetings(csv_path)
