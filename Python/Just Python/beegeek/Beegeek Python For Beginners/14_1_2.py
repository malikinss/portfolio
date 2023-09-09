'''
TODO: The online store provides express delivery for its products at a price of 1000 rubles for the first product and 120 rubles for each subsequent product.
Write a function get_shipping_cost(quantity), which takes as an argument the natural number quantity - the number of goods in the order - and returns the shipping cost.
'''


def get_shipping_cost(quantity):
    return 1000 + (quantity - 1) * 120


n = int(input())

print(get_shipping_cost(n))