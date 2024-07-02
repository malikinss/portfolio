'''
TODO:
        Dima really wants to eat, but he doesn't have much money.

        Help him determine the cheapest product and the store where it is sold.

        You have access to the prices.csv file, which contains information
        about the prices of products in various stores.

        The first column contains the name of the store, and the following
        columns contain the price of the corresponding product in this store:
            Shop;Cottage cheese;Buckwheat;Rice;Borodinsky bread;Apples;Dumplings;Oatmeal cookies;Spaghetti;Baked beans;Ice cream;Minced meat;Vareniki;Potato;Baton
            Pyaterochka;69;133;129;83;141;90;72;123;149;89;88;106;54;84
            Magnet;102;87;95;75;109;112;97;82;101;134;69;61;141;79
            ...

        Write a program that determines and displays the cheapest product and
        the name of the store where it is sold, in the following format:
            <product name>: <store name>

        If there are several the cheapest goods, then you should output the
        goods whose name is lower in the lexicographic comparison.

        If one product is sold in several stores at one minimum price, then
        you should output the store whose name is lower in the lexicographic comparison.

NOTE:
        The separator in the prices.csv file is a semicolon, and quotation
        marks are not used.

        Example of output:
            Strawberry yogurt: VkusVill

        When opening the file, use an explicit indication of the UTF-8
        encoding.
'''
import csv
from typing import List, Dict, Tuple

INPUT_FILE: str = '4_2_13/tests/prices.csv'


def read_csv(filename: str, delimiter: str = ',') -> List[Dict[str, str]]:
    """
    Reads a CSV file and returns its content as a list of dictionaries.

    Args:
        filename (str): The path to the CSV file.
        delimiter (str): The delimiter used in the CSV file.

    Returns:
        List[Dict[str, str]]: The content of the CSV file as a list of
        dictionaries.
    """
    with open(filename, 'r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=delimiter)
        return [row for row in reader]


def get_min_price_per_store(store_prices: Dict[str, str]) -> int:
    """
    Finds the minimum price of a product in a store.

    Args:
        store_prices (Dict[str, str]): Dictionary containing product prices in a store.

    Returns:
        int: The minimum price of a product in the store.
    """
    return min(int(price) for price in store_prices.values() if price.isdigit())


def get_store_and_min_price_goods(data: List[Dict[str, str]]) -> Dict[str, Dict[str, str]]:
    """
    Finds the minimum price of each product in each store.

    Args:
        data (List[Dict[str, str]]): List of dictionaries containing product prices in different stores.

    Returns:
        Dict[str, Dict[str, str]]: Dictionary where keys are store names and values are dictionaries
        containing product names and their minimum prices in each store.
    """
    min_prices_per_store: Dict[str, Dict[str, str]] = {}

    for row in data:
        store: str = row['Магазин']
        min_prices_per_store[store] = {}

        min_price: int = get_min_price_per_store(row)

        for key, value in row.items():
            if value.isdigit() and int(value) == min_price:
                min_prices_per_store[store][key] = value

    return min_prices_per_store


def get_main_min_price(store_prices: Dict[str, str]) -> int:
    """
    Finds the overall minimum price among all products in all stores.

    Args:
        store_prices (Dict[str, str]): Dictionary containing product prices in a store.

    Returns:
        int: The overall minimum price among all products in all stores.
    """
    return min(int(price) for price in store_prices.values() if price.isdigit())


def find_key_by_value(any_dict: Dict, any_value: any) -> any:
    """
    Finds a key in a dictionary based on its value.

    Args:
        any_dict (Dict): Dictionary to search.
        any_value (any): Value to find.

    Returns:
        any: The key corresponding to the given value.
    """
    for key, value in any_dict.items():
        if value == any_value:
            return key


def display_result(product: str, store: str) -> None:
    """
    Displays the result in a specified format.

    Args:
        product (str): The name of the product.
        store (str): The name of the store.
    """
    print(f'{product}: {store}')


def is_same_products(products: List[str]) -> bool:
    """
    Checks if all products are the same.

    Args:
        commodities (List[str]): List of products.

    Returns:
        bool: True if all products are the same, False otherwise.
    """
    return all(product == products[0] for product in products)


def get_cheapest_products(data_prices: Dict[str, Dict[str, str]]) -> Dict[str, str]:
    """
    Finds the products with the overall minimum price.

    Args:
        data_prices (Dict[str, Dict[str, str]]): Dictionary containing product
        prices in different stores.

    Returns:
        Dict[str, str]: Dictionary where keys are store names and values are
        product names with the minimum price.
    """
    overall_min_price: int = min(int(price) for store_prices in data_prices.values() for price in store_prices.values() if price.isdigit())
    cheapest_products: Dict[str, str] = {}

    for store, record in data_prices.items():
        for product, price in record.items():
            if price == str(overall_min_price):
                cheapest_products[store] = product

        return cheapest_products


def is_only_one(products: Dict[str, str]) -> bool:
    """
    Checks if there is only one product.

    Args:
        products (Dict[str, str]): Dictionary containing products.

    Returns:
        bool: True if there is only one product, False otherwise.
    """
    return len(products) == 1


def get_cheapest_store_and_product(products_per_shop: Dict[str, str]) -> Tuple[str, str]:
    """
    Finds the store and product with the overall minimum price.

    Args:
        products_per_shop (Dict[str, str]): Dictionary containing products and
        their prices in different stores.

    Returns:
        Tuple[str, str]: A tuple containing the name of the store and the name
        of the product with the minimum price.
    """
    cheapest_stores: List[str] = list(products_per_shop.keys())
    cheapest_products: List[str] = list(products_per_shop.values())

    if is_only_one(products_per_shop):
        store, product = next(iter(products_per_shop.items()))
    elif is_same_products(cheapest_products):
        store = min(cheapest_stores)
        product = products_per_shop[store]
    else:
        product = min(cheapest_products)
        store = find_key_by_value(products_per_shop, product)

    return store, product


def display_cheapest_product_and_store(data: List[Dict[str, str]]) -> None:
    """
    Displays the cheapest product and store.

    Args:
        data (List[Dict[str, str]]): List of dictionaries containing product
        prices in different stores.
    """
    min_prices: Dict[str, Dict[str, str]] = get_store_and_min_price_goods(data)
    cheapest_products_per_shop: Dict[str, str] = get_cheapest_products(min_prices)
    store, product = get_cheapest_store_and_product(cheapest_products_per_shop)
    display_result(product, store)


data: List[Dict[str, str]] = read_csv(INPUT_FILE, delimiter=';')
display_cheapest_product_and_store(data)
