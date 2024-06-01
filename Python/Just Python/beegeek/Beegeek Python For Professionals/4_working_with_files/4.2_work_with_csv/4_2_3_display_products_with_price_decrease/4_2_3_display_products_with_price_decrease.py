'''
TODO:
        November has come and many stores have started sales, but as
        many people know, often discounted products are more expensive
        than without it.

        You have access to the sales.csv file, which contains pricing
        data for various household appliances.

        The first column contains the product name, the second column
        contains the old price, and the third column contains the new
        discounted price:
            name;old_price;new_price
            Built-in dishwasher De'Longhi DDW 06S;23089;31862
            Falmec Afrodite 60/600 hood;27694;18001
            ...

        Write a program that displays the names of those products whose
        prices have decreased.
        The products must be in their original order, each on a separate
        line.

NOTE:
        The delimiter in the sales.csv file is a semicolon, and
        quotation marks are not used.
'''
import csv
from typing import List, Tuple


def read_csv_data(filename: str) -> List[Tuple[str, int, int]]:
    with open(filename, 'r', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file, delimiter=';')
        # Пропускаем заголовок
        next(reader)
        return [(row[0], int(row[1]), int(row[2])) for row in reader]


def display_products_with_price_decrease(products_data: List[Tuple[str, int, int]]) -> None:
    for name, old_price, new_price in products_data:
        if old_price > new_price:
            print(name)


# Чтение данных из файла и отображение продуктов с пониженной ценой
data = read_csv_data('sales.csv')
display_products_with_price_decrease(data)
