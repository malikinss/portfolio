'''
TODO:
        You have a list of staff tuples with data about employees of a
        certain company.

        The first element of the tuple is the name of the department
        The second is the first and last name of the employee working in
        this department.


        Complete the code below so that it determines how many employees work
        in each department and prints the names of all departments, indicating
        the corresponding number of employees for each.

        The departments should be in lexicographic order, each on a separate
        line, in the following format:
            <department>: <number of employees>

NOTE:
        The initial part of the response looks like this:
            Accounting: 17
            Developing: 7
            ...
'''
from collections import defaultdict
from typing import Dict, List, Tuple


def sort_dict_by_keys(data_dict: Dict[str, int]) -> Dict[str, int]:
    """
    Sorts a dictionary by its keys.

    Args:
        data_dict (Dict[str, int]): The dictionary to sort.

    Returns:
        Dict[str, int]: The sorted dictionary.
    """
    return dict(sorted(data_dict.items()))


def count_workers_per_department(data: List[Tuple[str, str]]) -> Dict[str, int]:
    """
    Counts the number of workers in each department.

    Args:
        data (List[Tuple[str, str]]): The list of tuples containing department
        and employee names.

    Returns:
        Dict[str, int]: A dictionary with departments as keys and the number
        of workers as values.
    """
    workers_per_department: Dict[str, int] = defaultdict(int)
    for department, _ in data:
        workers_per_department[department] += 1
    return sort_dict_by_keys(workers_per_department)


def print_workers_per_department(data: Dict[str, int]) -> None:
    """
    Prints the number of workers in each department.

    Args:
        data (Dict[str, int]): The dictionary with departments and the number
        of workers.
    """
    for department, amount in data.items():
        print(f'{department}: {amount}')


if __name__ == '__main__':
    # Given data
    staff = [('Sales', 'Robert Barnes'), ('Developing', 'Thomas Porter'),
             ('Accounting', 'James Wilkins'), ('Sales', 'Connie Reid'),
             ('Accounting', 'Brenda Davis'), ('Developing', 'Miguel Norris'),
             ('Accounting', 'Linda Hudson'), ('Developing', 'Deborah George'),
             ('Developing', 'Nicole Watts'), ('Marketing', 'Billy Lloyd'),
             ('Sales', 'Charlotte Cox'), ('Marketing', 'Bernice Ramos'),
             ('Sales', 'Jose Taylor'), ('Sales', 'Katie Warner'),
             ('Accounting', 'Steven Diaz'), ('Accounting', 'Kimberly Reynolds'),
             ('Accounting', 'John Watts'), ('Accounting', 'Dale Houston'),
             ('Developing', 'Arlene Gibson'), ('Marketing', 'Joyce Lawrence'),
             ('Accounting', 'Rosemary Garcia'), ('Marketing', 'Ralph Morgan'),
             ('Marketing', 'Sam Davis'), ('Marketing', 'Gail Hill'),
             ('Accounting', 'Michelle Wright'), ('Accounting', 'Casey Jenkins'),
             ('Sales', 'Evelyn Martin'), ('Accounting', 'Aaron Ferguson'),
             ('Marketing', 'Andrew Clark'), ('Marketing', 'John Gonzalez'),
             ('Developing', 'Wilma Woods'), ('Sales', 'Marie Cooper'),
             ('Accounting', 'Kay Scott'), ('Sales', 'Gladys Taylor'),
             ('Accounting', 'Ann Bell'), ('Accounting', 'Craig Wood'),
             ('Accounting', 'Gloria Higgins'), ('Marketing', 'Mario Reynolds'),
             ('Marketing', 'Helen Taylor'), ('Marketing', 'Mary King'),
             ('Accounting', 'Jane Jackson'), ('Marketing', 'Carol Peters'),
             ('Sales', 'Alicia Mendoza'), ('Accounting', 'Edna Cunningham'),
             ('Developing', 'Joyce Rivera'), ('Sales', 'Joseph Lee'),
             ('Sales', 'John White'), ('Marketing', 'Charles Bailey'),
             ('Sales', 'Chester Fernandez'), ('Sales', 'John Washington')]

    # Calculate total workers for each department
    workers_per_department = count_workers_per_department(staff)

    # Display total workers for each department
    print_workers_per_department(workers_per_department)
