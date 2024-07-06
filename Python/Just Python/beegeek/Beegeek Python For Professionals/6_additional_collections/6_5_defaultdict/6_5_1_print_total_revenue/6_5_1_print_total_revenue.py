'''
TODO:
        You are given a list of data tuples containing revenue data for some
        educational resource.
        The first element of the tuple is the product name, and the second
        element is the revenue in dollars.
        Expand the code below to determine how much total revenue each product
        brought in and print the names of all the products, with the
        corresponding total revenue for each.
        The products should be listed lexicographically, each on a separate
        line, in the following format:
            <product>: $<total revenue>

NOTE:
        The initial part of the response looks like this:
            Books: $7969
            Courses: $2991
            ...
'''
from collections import defaultdict
from typing import Dict, List, Tuple


def calculate_total_revenue(data: List[Tuple[str, int]]) -> Dict[str, int]:
    """
    Calculates the total revenue for each product.

    Args:
        data (List[Tuple[str, int]]): A list of tuples containing product name
        and revenue.

    Returns:
        Dict[str, int]: A dictionary mapping product names to their total
        revenue.
    """
    total_revenue = defaultdict(int)

    for product, revenue in data:
        total_revenue[product] += revenue

    # Sort dictionary by keys (product names)
    return dict(sorted(total_revenue.items()))


def print_total_revenue(total_revenue: Dict[str, int]) -> None:
    """
    Prints the total revenue for each product in a specified format.

    Args:
        total_revenue (Dict[str, int]): A dictionary mapping product names to
        their total revenue.
    """
    for product, revenue in total_revenue.items():
        print(f'{product}: ${revenue}')


if __name__ == '__main__':
    # Given data
    data = [
        ('Books', 1343), ('Books', 1166), ('Merch', 616),
        ('Courses', 966), ('Merch', 1145), ('Courses', 1061),
        ('Books', 848), ('Courses', 964), ('Tutorials', 832),
        ('Merch', 642), ('Books', 815), ('Tutorials', 1041),
        ('Books', 1218), ('Tutorials', 880), ('Books', 1003),
        ('Merch', 951), ('Books', 920), ('Merch', 729),
        ('Tutorials', 977), ('Books', 656)
    ]

    # Calculate total revenue for each product
    total_revenue = calculate_total_revenue(data)

    # Display total revenue for each product
    print_total_revenue(total_revenue)
