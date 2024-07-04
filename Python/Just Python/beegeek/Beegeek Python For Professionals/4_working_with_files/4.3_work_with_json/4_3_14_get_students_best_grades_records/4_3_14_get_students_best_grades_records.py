'''
TODO:
        You have access to the exam_results.csv file, which contains
        information about a past exam at a certain educational institution.

        The first column contains the student's name;
        The second column contains the last name;
        The third column contains the exam grade;
        The fourth column contains the date and time of the exam
        in the next format:
            YYYY-MM-DD HH:MM:SS
        The fifth column contains the email address:
            name,surname,score,date_and_time,email
            Jayson,Edwards,2,2021-11-10 10:00:00,sonnen@yahoo.com
            April,Sims,3,2021-11-01 11:00:00,retoh@outlook.com
            ...

        Each student has the right to retake the exam twice, so it can appear
        in the original file up to three times with different grades and
        different dates and times of the exam.

        Write a program that determines the best grade for each student, as
        well as the date and time it was received.

        The program should create a list of dictionaries, each containing the
        following key-value pairs:
            name — student's first name
            surname — student's last name
            best_score — best grade for the exam
            date_and_time — date and time of receiving the best grade in
                            the original format
            email — email address

        The program should write the resulting list to the best_scores.json
        file, and the dictionaries in the list should be arranged in
        lexicographic order of email names.

NOTE:
        If the student received the same grade on the retake as the previous
        time, then the date should be specified as the retake date.

        A comma is used as a separator in the exam_results.csv file, and
        quotation marks are not used.

        The initial part of the best_scores.json file looks like this:
            [
                {
                    "name": "Stephen",
                    "surname": "Farley",
                    "best_score": 3,
                    "date_and_time": "2021-11-12 12:00:00",
                    "email": "aardo@mac.com"
                },
                {
                    "name": "Kaylen",
                    "surname": "Horne",
                    "best_score": 4,
                    "date_and_time": "2021-11-09 11:00:00",
                    "email": "aaribaud@att.net"
                },
                ...
            ]
'''
import json
import csv
from typing import Dict, List
from datetime import datetime


TIME_FORMAT = '%Y-%m-%d %H:%M:%S'


def read_csv(filename: str, delimiter: str = ',') -> List[Dict[str, str]]:
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


def write_json_file(data: Dict[str, List[str]], file_path: str) -> None:
    """
    Write JSON data to a file.

    Args:
        data (Dict[str, List[str]]): JSON data to be written.
        file_path (str): Path to the output JSON file.
    """
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=3)


def get_all_student_records(records: List[Dict[str, str]],
                            name: str,
                            surname: str) -> List[Dict[str, str]]:
    """
    Get all records for a specific student.

    Args:
        records: List of records.
        name: Student's name.
        surname: Student's surname.

    Returns:
        List of records for the student.
    """
    return [record for record in records if record['name'] == name and record['surname'] == surname]


def create_grade_record_from_info(student_info: Dict[str, str],
                                  best_score: float) -> Dict[str, str]:
    """Create a grade record from student information."""
    grade_record = {}

    for key, value in student_info.items():
        if key != 'score':
            grade_record[key] = value
        else:
            grade_record['best_score'] = best_score

    return grade_record


def find_records_with_best_grade(records: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """Find records with the best grade."""
    best_grade = max(int(record['score']) for record in records)

    top_records = [create_grade_record_from_info(record, best_grade) for record in records if int(record['score']) == best_grade]

    return top_records


def get_record_with_latest_date(records: List[Dict[str, str]]) -> Dict[str, str]:
    """Get the latest record based on the date and time."""
    return max(records, key=lambda x: datetime.strptime(x['date_and_time'], '%Y-%m-%d %H:%M:%S'))


def get_student_best_grade_record(records: List[Dict[str, str]]) -> Dict[str, str]:
    """Get the best grade record for the student."""
    best_grade_records = find_records_with_best_grade(records)
    if len(best_grade_records) > 1:
        return get_record_with_latest_date(best_grade_records)
    return best_grade_records[0]


def is_person_exist(records, name, surname):
    for record in records:
        if record['name'] == name and record['surname'] == surname:
            return True

    return False


def get_students_best_grades_records(records):
    students_best_records = []

    for record in records:
        name = record['name']
        surname = record['surname']

        if not is_person_exist(students_best_records, name, surname):
            student_records = get_all_student_records(records, name, surname)

            best_record = get_student_best_grade_record(student_records)
            students_best_records.append(best_record)

    return sorted(students_best_records, key=lambda x: x['email'])


if __name__ == "__main__":
    input_file = 'exam_results.csv'
    output_file = 'best_scores.json'

    data = read_csv(input_file)
    best_records = get_students_best_grades_records(data)
    write_json_file(best_records, output_file)
