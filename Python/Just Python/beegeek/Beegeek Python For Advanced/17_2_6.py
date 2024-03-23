'''
TODO:   You have access to the text file 'prices.txt' with information about the order from the online store. 
        In it, each line is divided into three columns using the tab character (\t):

        1. product name;
        2. the quantity of the product (integer);
        3. the price (in rubles) of the product for 1 piece (integer).

        Write a program that displays the total cost of the order.

NOTE:   Assume that the executable program and the specified file are in the same folder.
'''


def get_data_from_file(file_name):
    given_file = open(file_name, 'rt', encoding='utf-8') # open file for text reading
    content = [row_from_file.rstrip() for row_from_file in given_file.readlines()] # get list of rows from file
    given_file.close() # free memmory

    return content

def get_total_price_of_order(order_list):
    price = 0

    for product in order_list:
        product_list = product.split()
        price += int(product_list[1]) * int(product_list[2])

    return price

data = get_data_from_file('prices.txt')

print()
print('result =',get_total_price_of_order(data))
print()