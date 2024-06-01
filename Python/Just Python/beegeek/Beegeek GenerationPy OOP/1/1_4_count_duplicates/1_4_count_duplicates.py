'''
TODO:
        Arthur has a small collection of Pokemon cards, some of which
        are duplicates.
        He wants to keep one card of each type and sell the rest.

        Write a program that determines how many duplicates Arthur can
        sell from his collection.

        Input:
            The program receives an arbitrary number of lines
            representing a collection of Pokemon cards.
            Each line contains the name of a Pokemon from the card.

        Output:
            The program should output a single number — the number of
            cards that can be sold from this collection to keep one card
            of each type.
'''
import sys


def read_input() -> list[str]:
    """Reads input from stdin and returns a list of stripped lines."""
    return [line.strip() for line in sys.stdin.readlines()]


def count_duplicates(given_cards: list[str]) -> int:
    unique_cards = set()

    for card in given_cards:
        if card not in unique_cards:
            unique_cards.add(card)

    # Total cards minus unique cards equals duplicate cards
    return len(given_cards) - len(unique_cards)


given_cards = read_input()
duplicates = count_duplicates(given_cards)
print(duplicates)
