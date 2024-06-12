'''
TODO:
        You have access to the name_log.csv file, which contains the user name
        change logs.
        The first column contains the changed user name.
        The second column contains the email address.
        The third column contains the date and time of the change.

        The user cannot change the email, only the name:
            username,email,dtime
            rare_charles6,charlesthompson@inbox.ru,11/15/2021 08:15
            busy_patricia5,patriciasmith@bk.ru,11/07/2021 08:07
            ...

        Write a program that selects only the most recent entries for each
        user from the name_log.csv file and writes them to the
        new_name_log.csv file.

        The first row of the new_name_log.csv file should contain the same
        column headers as in the name_log.csv file.

        The logs in the final file should be arranged in lexicographic order
        of the user email address.

NOTE:
        For some users, there is only one entry in the source file, and then
        only that entry should be written to the final file; for some users,
        there are several entries with different names.

        For example, a user with the email address c3po@gmail.com changed
        their name several times:
            C=3PO,c3po@gmail.com,11/16/2021 5:10 PM
            C3PO,c3po@gmail.com,11/16/2021 5:15 PM
            C-3PO,c3po@gmail.com,11/16/2021 5:24 PM

        Of these three entries, only one should be written to the final
        file - the most recent one:
            C-3PO,c3po@gmail.com,11/16/2021 5:24 PM

        The separator in the name_log.csv file is a comma, and quotation marks
        are not used.
'''
import csv
from datetime import datetime as dt
from typing import List, Dict


INPUT_CSV_PATH = '4_2_10/tests/name_log.csv'
OUTPUT_CSV_PATH = '4_2_10/tests/new_name_log.csv'

TIME_MASK = '%d/%m/%Y %H:%M'


def read_csv(filename: str,
             delimiter: str = ',') -> List[Dict[str, str]]:
    """
    Reads a CSV file and returns its content as a list of dictionaries.

    Args:
        filename: The path to the CSV file.
        delimiter: The delimiter used in the CSV file.

    Returns:
        The content of the CSV file as a list of dictionaries.
    """
    with open(filename, 'r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=delimiter)
        return [row for row in reader]


def write_csv(data: List[Dict[str, str]],
              filename: str,
              columns: List[str],
              delimiter: str = ',') -> None:
    """
    Writes data to a CSV file.

    Args:
        data: The data to write, as a list of dictionaries.
        filename: The path to the output CSV file.
        columns: The column names to use in the CSV file.
        delimiter: The delimiter to use in the CSV file.
    """
    with open(filename, 'w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file,
                                fieldnames=columns,
                                delimiter=delimiter)
        writer.writeheader()
        writer.writerows(data)


def group_logs_by_email(data: List[Dict[str, str]]) -> Dict[str, List[Dict[str, str]]]:
    """
    Groups log entries by user email.

    Args:
        data: The log entries to group.

    Returns:
        A dictionary mapping each email to a list of its log entries.
    """
    logs_per_user = {}
    for record in data:
        email = record['email']
        logs_per_user.setdefault(email, []).append(record)
    return logs_per_user


def find_latest_date(dates: List[str]) -> dt:
    """
    Finds the latest date from a list of date strings.

    Args:
        dates: A list of date strings in the format specified by TIME_MASK.

    Returns:
        The latest date as a datetime object.
    """
    return max((dt.strptime(date, TIME_MASK) for date in dates), key=lambda x: x)


def extract_user_dates(logs: List[Dict[str, str]]) -> List[str]:
    """
    Extracts dates from a list of log entries.

    Args:
        logs: A list of log entries.

    Returns:
        A list of date strings extracted from the log entries.
    """
    return [log['dtime'] for log in logs]


def find_latest_user_log(logs: List[Dict[str, str]]) -> Dict[str, str]:
    """
    Finds the latest log entry for a user.

    Args:
        logs: A list of log entries for a user.

    Returns:
        The latest log entry.
    """
    dates = extract_user_dates(logs)
    latest_date = find_latest_date(dates).strftime(TIME_MASK)

    return next(log for log in logs if log['dtime'] == latest_date)


def extract_latest_logs(data: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """
    Extracts the latest log entry for each user.

    Args:
        data: All log entries.

    Returns:
        A list of the latest log entry for each user.
    """
    logs_per_user = group_logs_by_email(data)
    latest_logs = []

    for logs in logs_per_user.values():
        if len(logs) == 1:
            latest_logs.append(logs[0])
        else:
            latest_logs.append(find_latest_user_log(logs))

    return latest_logs


def sort_by_email(data: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """
    Sorts log entries by email address.

    Args:
        data: The log entries to sort.

    Returns:
        The log entries sorted by email address.
    """
    return sorted(data, key=lambda x: x['email'])


data = read_csv(INPUT_CSV_PATH, delimiter=',')
headers = list(data[0].keys())
latest_logs = sort_by_email(extract_latest_logs(data))
write_csv(latest_logs, OUTPUT_CSV_PATH, headers)
