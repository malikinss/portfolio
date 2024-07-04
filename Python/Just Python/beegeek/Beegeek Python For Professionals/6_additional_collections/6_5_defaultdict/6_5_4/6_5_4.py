'''
TODO:
        The BEEGEEK online school holds chess competitions every summer, during which statistics are kept of wins and losses.
        
        Each game is described by a tuple of two elements, where:
            - the first element is the name of the winning student
            - the second element is the name of the losing student

        Implement a wins() function that takes one argument:
        pairs - is an iterable whose elements are tuples, each of which is a pair of names of the winner and loser

        The function should return a dictionary in which the key is the name of the student, and the value is a set of names of the students he or she defeated.

NOTE:
        It is guaranteed that each game ends with a victory of one of the students, i.e. there can be no draws.

        The elements in the dictionary returned by the function can be in any order.
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
