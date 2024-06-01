'''
TODO:
        You have access to the file salary_data.csv, which contains
        anonymous information about employee salaries in various
        companies.

        The first column contains the company name, and the second
        column contains the salary of the next employee:
            company_name;salary
            Atos;135000
            HighTech;24400
            Philax;128600
            Inline Group;43900
            IBS;70600
            Oracle;131600
            Atos;91000
            ...

        Write a program that sorts the companies by increasing average
        salary of their employees and displays their names, each on a
        separate line.
        If two companies have the same average salaries, they should be
        arranged in lexicographic order of their names.

NOTE:
        The average salary of a company is defined as the ratio of the
        sum of all salaries to their number.

        The separator in the file salary_data.csv is a semicolon, and
        quotation marks are not used.
'''
import csv
from collections import defaultdict
from typing import List, Tuple, Dict


def read_csv_data(filename: str) -> List[Tuple[str, int]]:
    """
    Reads data from a CSV file and returns a list of tuples with company
    names and salaries.

    :param filename: Path to the CSV file.
    :return: List of tuples (company name, salary).
    """
    with open(filename, 'r', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file, delimiter=';')
        # Пропуск заголовка
        next(reader)
        return [(row[0], int(row[1])) for row in reader]


def get_average_value(values: List[int]) -> float:
    """
    Calculates the average of a list of numbers.

    :param values: List of numbers.
    :return: Average value.
    """
    return sum(values) / len(values)


def get_salaries_per_company(data: List[Tuple[str, int]]) -> Dict[str, List[int]]:
    """
    Creates a dictionary with company names and lists of employee salaries.

    :param data: List of tuples (company name, salary).
    :return: Dictionary {company name: salary list}.
    """
    salaries_per_company = defaultdict(list)
    for company_name, salary in data:
        salaries_per_company[company_name].append(salary)
    return salaries_per_company


def calculate_average_salaries(salaries_per_company: Dict[str, List[int]]) -> Dict[str, float]:
    """
    Calculates average salaries for each company.

    :param salaries_per_company: Dictionary {company name: list of salaries}.
    :return: Dictionary {company name: average salary}.
    """
    return {company: get_average_value(salaries) for company, salaries in salaries_per_company.items()}


def display_sorted_companies(sorted_data: List[Tuple[str, float]]) -> None:
    """
    Displays company names sorted by increasing average salary.

    :param sorted_data: List of tuples (company name, average salary), sorted by salary.
    """
    for company_name, _ in sorted_data:
        print(company_name)


def sort_companies_by_increasing_avg_salary(data: List[Tuple[str, int]]) -> List[Tuple[str, float]]:
    """
        Sorts companies by increasing average salary.

        :param data: List of tuples (company name, salary).
        :return: Sorted list of tuples (company name, average salary).
    """
    salaries_per_company = get_salaries_per_company(data)
    average_salaries = calculate_average_salaries(salaries_per_company)
    return sorted(average_salaries.items(), key=lambda item: (item[1], item[0]))


FILE_PATH = 'salary_data.csv'

if __name__ == "__main__":
    data = read_csv_data(FILE_PATH)
    sorted_salaries = sort_companies_by_increasing_avg_salary(data)
    display_sorted_companies(sorted_salaries)
