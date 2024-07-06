'''
TODO:
        You have access to a named tuple User, which contains data about
        a user of some resource.

        The first element of the named tuple is the user's name
        The second is the last name
        The third is the email address
        The fourth is the subscription status

        A list users containing these tuples is also available.

        Supplement the code below so that it displays data about each user
        from this list, sorting them by subscription status from expensive
        to cheap, and if the statuses match, in lexicographic order of
        email addresses.

        Data about each user must be specified in the following format:
            <first name> <last name>
            Email: <email address>
            Plan: <subscription status>

        There must be an empty line between data for two different users.

NOTE:
        The most expensive subscription is Gold, then Silver, Bronze and Basic.

        The initial part of the response looks like this (use two spaces
        for indentation):
            Kathleen Lyons
              Email: balchen@att.net
              Plan: Gold

            William Townsend
              Email: kosact@verizon.net
              Plan: Gold
            ...
'''
from typing import List
from collections import namedtuple


User = namedtuple('User', ['name', 'surname', 'email', 'plan'])

users = [User('Mary', 'Griffin', 'sonnen@yahoo.com', 'Basic'),
         User('Brenda', 'Young', 'retoh@outlook.com', 'Silver'),
         User('Kathleen', 'Lyons', 'balchen@att.net', 'Gold'),
         User('Pamela', 'Hicks', 'corrada@sbcglobal.net', 'Silver'),
         User('William', 'Townsend', 'kosact@verizon.net', 'Gold'),
         User('Clayton', 'Morris', 'berserk@yahoo.com', 'Silver'),
         User('Dorothy', 'Dennis', 'sequin@live.com', 'Gold'),
         User('Tyler', 'Walker', 'noahb@comcast.net', 'Basic'),
         User('Joseph', 'Moore', 'ylchang@sbcglobal.net', 'Silver'),
         User('Kenneth', 'Richardson', 'tbusch@me.com', 'Bronze'),
         User('Stephanie', 'Bush', 'neuffer@live.com', 'Gold'),
         User('Gregory', 'Hughes', 'juliano@att.net', 'Basic'),
         User('Tracy', 'Wallace', 'sblack@me.com', 'Silver'),
         User('Russell', 'Smith', 'isaacson@comcast.net', 'Bronze'),
         User('Megan', 'Patterson', 'hoangle@outlook.com', 'Basic')]


def get_fullname(user: User) -> str:
    """
    Returns the full name of the user.

    Args:
        user (User): The user namedtuple.

    Returns:
        str: The full name of the user.
    """
    return f'{user.name} {user.surname}'


def sort_users(users: List[User]) -> List[User]:
    """
    Sorts the list of users by subscription status and email.

    Args:
        users (List[User]): The list of user namedtuples.

    Returns:
        List[User]: The sorted list of user namedtuples.
    """
    plan_order = {'Gold': 1, 'Silver': 2, 'Bronze': 3, 'Basic': 4}
    sorted_users = sorted(users, key=lambda user: (plan_order[user.plan], user.email))
    return sorted_users


def print_user_details(user: User) -> None:
    """
    Prints the details of a user in the specified format.

    Args:
        user (User): The user namedtuple.
    """
    fullname = get_fullname(user)
    print(fullname)

    for field, value in user._asdict().items():
        if field in ('name', 'surname'):
            continue

        print(f'  {field.capitalize()}: {value}')

    print()


def display_sorted_users(users: List[User]) -> None:
    """
    Sorts and displays the details of users in the specified format.

    Args:
        users (List[User]): The list of user namedtuples.
    """
    sorted_users = sort_users(users)
    for user in sorted_users:
        print_user_details(user)


display_sorted_users(users)
