'''
TODO:
        A sequence of dates is given. Write a program that determines the
        order in which dates appear in a given sequence.

        Input format:
            An arbitrary number of lines (two or more) are supplied to
            the program input;
            each line contains a date in the DD.MM.YYYY format.

        Output format:
            The program should output the text:
                ASC - if the dates in the entered sequence are strictly
                in ascending order
                DESC - if the dates in the entered sequence are strictly
                in descending order
                MIX - if the dates in the entered sequence are in neither
                ascending nor descending order

        The ASC and DESC parameters are used in SQL to sort in ascending
        and descending order respectively.
'''
import sys
from datetime import datetime
from typing import List


def read_input() -> List[str]:
    """Reads input from stdin and returns a list of stripped lines."""
    return [line.strip() for line in sys.stdin.readlines()]


def string_to_date(date_string: str) -> datetime.date:
    """Converts a date string in the format DD.MM.YYYY to a date object."""
    date_obj = datetime.strptime(date_string, '%d.%m.%Y')
    return date_obj.date()


def parse_dates(data: List[str]) -> List[datetime.date]:
    """Parses a list of date strings to a list of date objects."""
    return [string_to_date(record) for record in data]


def is_strictly_asc_order(dates: List[datetime.date]) -> bool:
    """Checks if the list of dates is in strictly ascending order."""
    return all(dates[i] < dates[i + 1] for i in range(len(dates) - 1))


def is_strictly_desc_order(dates: List[datetime.date]) -> bool:
    """Checks if the list of dates is in strictly descending order."""
    return all(dates[i] > dates[i + 1] for i in range(len(dates) - 1))


def print_dates_order(dates: List[datetime.date]) -> None:
    """Determines and displays the order type of the given dates."""
    if is_strictly_asc_order(dates):
        print('ASC')
    elif is_strictly_desc_order(dates):
        print('DESC')
    else:
        print('MIX')


def main() -> None:
    """Main function to execute the date order checking program."""
    given_data = read_input()
    given_dates = parse_dates(given_data)
    print_dates_order(given_dates)


if __name__ == "__main__":
    main()
