'''
TODO:
        You have access to a list of tuples staff_broken with data on
        employees of a certain company.

        The first element of the tuple is the name of the department
        The second is the first and last name of the employee working in this
        department

        Some employees may appear in the list more than once.

        Complete the code below so that it groups employees by their
        departments and displays the names of all departments, indicating the
        first and last names of their employees for each.

        Departments and the names of employees within those departments should
        be listed lexicographically, each on a separate line, in the following
        format:
        <department>: <first> <last>, <first> <last>, ...

NOTE:
        The initial portion of the response should look like this:
            Accounting: Aaron Ferguson, Ann Bell, Brenda Davis, Casey Jenkins, Craig Wood, Dale Houston, Edna Cunningham, Gloria Higgins, James Wilkins, Jane Jackson, John Watts, Kay Scott, Kimberly Reynolds, Linda Hudson, Michelle Wright, Rosemary Garcia, Steven Diaz

            Developing: Arlene Gibson, Deborah George, Joyce Rivera, Miguel Norris, Nicole Watts, Thomas Porter, Wilma Woods
            ...
'''
from collections import defaultdict
from typing import Dict, List, Tuple, Set


def sort_dict_keys(data_dict: Dict[str, Set[str]]) -> Dict[str, Set[str]]:
    """
    Sorts a dictionary by its keys.

    Args:
        data_dict (Dict[str, Set[str]]): The dictionary to sort.

    Returns:
        Dict[str, Set[str]]: The sorted dictionary.
    """
    return dict(sorted(data_dict.items()))


def sort_department_workers(workers_per_department: Dict[str, Set[str]]) -> Dict[str, List[str]]:
    """
    Sorts the workers in each department and returns a sorted dictionary.

    Args:
        workers_per_department (Dict[str, Set[str]]): The dictionary
        containing workers per department.

    Returns:
        Dict[str, List[str]]: The sorted dictionary with sorted lists of
        workers.
    """
    sorted_dict = sort_dict_keys(workers_per_department)
    for department in sorted_dict:
        sorted_dict[department] = sorted(sorted_dict[department])
    return sorted_dict


def group_workers_by_department(data: List[Tuple[str, str]]) -> Dict[str, Set[str]]:
    """
    Groups workers by their departments.

    Args:
        data (List[Tuple[str, str]]): The list of tuples containing department
        and worker name.

    Returns:
        Dict[str, Set[str]]: A dictionary grouping workers by department.
    """
    workers_per_department = defaultdict(set)

    for department, worker in data:
        workers_per_department[department].add(worker)

    return workers_per_department


def print_department_workers(workers_per_department: Dict[str, List[str]]) -> None:
    """
    Prints the workers grouped by their departments.

    Args:
        workers_per_department (Dict[str, List[str]]): The dictionary with
        departments and the list of workers.
    """
    for department, workers in workers_per_department.items():
        print(f'{department}: {", ".join(workers)}')


if __name__ == '__main__':
    # Given data
    staff = [
        ('Developing', 'Miguel Norris'), ('Sales', 'Connie Reid'),
        ('Sales', 'Joseph Lee'), ('Marketing', 'Carol Peters'),
        ('Accounting', 'Linda Hudson'), ('Accounting', 'Ann Bell'),
        ('Marketing', 'Ralph Morgan'), ('Accounting', 'Gloria Higgins'),
        ('Developing', 'Wilma Woods'), ('Developing', 'Wilma Woods'),
        ('Marketing', 'Bernice Ramos'), ('Marketing', 'Joyce Lawrence'),
        ('Accounting', 'Craig Wood'), ('Developing', 'Nicole Watts'),
        ('Sales', 'Jose Taylor'), ('Accounting', 'Linda Hudson'),
        ('Accounting', 'Edna Cunningham'), ('Sales', 'Jose Taylor'),
        ('Marketing', 'Helen Taylor'), ('Accounting', 'Kimberly Reynolds'),
        ('Marketing', 'Mary King'), ('Sales', 'Joseph Lee'),
        ('Accounting', 'Gloria Higgins'), ('Marketing', 'Andrew Clark'),
        ('Accounting', 'John Watts'), ('Accounting', 'Rosemary Garcia'),
        ('Accounting', 'Steven Diaz'), ('Marketing', 'Mary King'),
        ('Sales', 'Gladys Taylor'), ('Developing', 'Thomas Porter'),
        ('Accounting', 'Brenda Davis'), ('Sales', 'Connie Reid'),
        ('Sales', 'Alicia Mendoza'), ('Marketing', 'Mario Reynolds'),
        ('Sales', 'John White'), ('Developing', 'Joyce Rivera'),
        ('Accounting', 'Steven Diaz'), ('Developing', 'Arlene Gibson'),
        ('Sales', 'Robert Barnes'), ('Sales', 'Charlotte Cox'),
        ('Accounting', 'Craig Wood'), ('Marketing', 'Carol Peters'),
        ('Marketing', 'Ralph Morgan'), ('Accounting', 'Kay Scott'),
        ('Sales', 'Evelyn Martin'), ('Marketing', 'Billy Lloyd'),
        ('Sales', 'Gladys Taylor'), ('Developing', 'Deborah George'),
        ('Sales', 'Charlotte Cox'), ('Marketing', 'Sam Davis'),
        ('Sales', 'John White'), ('Sales', 'Marie Cooper'),
        ('Marketing', 'John Gonzalez'), ('Sales', 'John Washington'),
        ('Sales', 'Chester Fernandez'), ('Sales', 'Alicia Mendoza'),
        ('Sales', 'Katie Warner'), ('Accounting', 'Jane Jackson'),
        ('Sales', 'Chester Fernandez'), ('Marketing', 'Charles Bailey'),
        ('Marketing', 'Gail Hill'), ('Accounting', 'Casey Jenkins'),
        ('Accounting', 'James Wilkins'), ('Accounting', 'Casey Jenkins'),
        ('Marketing', 'Mario Reynolds'), ('Accounting', 'Aaron Ferguson'),
        ('Accounting', 'Kimberly Reynolds'), ('Sales', 'Robert Barnes'),
        ('Accounting', 'Aaron Ferguson'), ('Accounting', 'Jane Jackson'),
        ('Developing', 'Deborah George'), ('Accounting', 'Michelle Wright'),
        ('Accounting', 'Dale Houston')
    ]

    # Group workers by department
    grouped_workers = group_workers_by_department(staff)

    # Sort departments and workers within each department
    sorted_workers = sort_department_workers(grouped_workers)

    # Print the sorted workers by department
    print_department_workers(sorted_workers)
