'''
TODO:
        The BEEGEEK online school holds chess competitions every summer,
        during which statistics are kept of wins and losses.

        Each game is described by a tuple of two elements, where:
            - the first element is the name of the winning student
            - the second element is the name of the losing student

        Implement a wins() function that takes one argument:
        pairs - is an iterable whose elements are tuples, each of which is a
        pair of names of the winner and loser

        The function should return a dictionary in which the key is the name
        of the student, and the value is a set of names of the students he or
        she defeated.

NOTE:
        It is guaranteed that each game ends with a victory of one of the
        students, i.e. there can be no draws.

        The elements in the dictionary returned by the function can be in
        any order.
'''
from collections import defaultdict
from typing import Dict, Tuple, Set, Iterable


def wins(games: Iterable[Tuple[str, str]]) -> Dict[str, Set[str]]:
    """
    Computes the winners and their defeated opponents from a list of games.

    Args:
        games (Iterable[Tuple[str, str]]): An iterable containing tuples,
        each representing a game with the winner and loser.

    Returns:
        Dict[str, Set[str]]: A dictionary where the key is the name of the
        student and the value is a set of names of the students they defeated.
    """
    winners_dict = defaultdict(set)

    for winner, loser in games:
        winners_dict[winner].add(loser)

    return winners_dict


def print_results(results: Dict[str, Set[str]]) -> None:
    """
    Prints the results of the games in a formatted manner.

    Args:
        results (Dict[str, Set[str]]): A dictionary where the key is the name
        of the student and the value is a set of names of the students they
        defeated.
    """
    for winner, losers in sorted(results.items()):
        print(winner, '->', *sorted(losers))


if __name__ == '__main__':
    # Example games data
    result = wins([('Артур', 'Дима'),
                   ('Артур', 'Тимур'),
                   ('Артур', 'Анри'),
                   ('Дима', 'Артур')])

    # Print formatted results
    print_results(result)
