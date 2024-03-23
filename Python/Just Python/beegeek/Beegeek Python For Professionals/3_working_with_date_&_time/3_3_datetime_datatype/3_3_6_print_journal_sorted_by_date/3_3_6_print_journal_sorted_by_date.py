'''
TODO:   
        You have access to the text file diary.txt, in which the astronaut wrote down small reports for the day. 
        
        He could write each new report either at the beginning of the file, or in the middle, or at the end. 
        
        All reports are separated by a blank line. 
        
        Each new report begins with a line with the date and time in the format DD.MM.YYYY; HH:MM, followed by events that occurred on the specified day.

        Write a program that puts all the astronaut's records in chronological order and displays the result.

NOTE:   
        When opening a file, use an explicit UTF-8 encoding.

'''

from datetime import datetime

def read_data_from_file(file_name):
    try:
        with open(file_name, 'rt', encoding='utf-8') as given_file:
            content = [line.rstrip() for line in given_file.readlines()]
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        content = []

    return content

def is_correct_date(day, month, year):
    is_correct_day  = 1 <= day <= 31
    is_correct_month = 1 <= month <= 12
    is_correct_year = 1900 <= year <= 9999

    return all([is_correct_day, is_correct_month, is_correct_year])

def is_correct_time(hour, minute):
    is_correct_hour = 0 <= hour <= 23
    is_correct_minute = 0 <= minute <= 59

    return all([is_correct_hour, is_correct_minute])

def is_datetime_as_string(given_string):
    try:
        given_date, given_time = given_string.split('; ')
        day, month, year = map(int, given_date.split('.'))
        hour, minute = map(int, given_time.split(':'))

        correct_date = is_correct_date(day, month, year)
        correct_time = is_correct_time(hour, minute)

        return all([correct_date, correct_time])

    except (ValueError, IndexError):
        return False

def parse_datetime_string(given_string):
    try:
        return datetime.strptime(given_string, '%d.%m.%Y; %H:%M')
    except ValueError:
        print(f"Error: Invalid date-time format - {given_string}")
        return None
    
def get_journal_records(data):
    journal_records = {}
    key = None

    for row in data:
        if is_datetime_as_string(row):
            key = parse_datetime_string(row)
            journal_records[key] = []
        else: 
            journal_records[key].append(row)     
    
    return journal_records        

def print_journal_sorted_by_date(journal):
    sorted_keys = sorted(journal.keys())
    amount_of_records = len(sorted_keys)
    record_number = 0

    for key in sorted_keys:
        record_number += 1
        print(key.strftime('%d.%m.%Y; %H:%M'))

        value = journal.get(key)

        for row in value:
            print(row)

        if record_number != amount_of_records:
            print()

def remove_empty_lines(data):
    return [row for row in data if row != '']
    
file_path = 'diary.txt'
given_data = read_data_from_file(file_path)
given_data = remove_empty_lines(given_data)    
journal_records = get_journal_records(given_data)

print_journal_sorted_by_date(journal_records)