'''
TODO:
        You have a dictionary data with an even number of elements.
        Complete the code below so that it prints this dictionary, ordering
        its elements according to the following rule:
            first, last, second, second-to-last, third, and so on.

NOTE:
        For example, if the dictionary data were:
            data = OrderedDict(key1='value1', key2='value2',
                               key3='value3', key4='value4')
        then the program would output (prior to Python 3.12):
            OrderedDict([('key1', 'value1'), ('key4', 'value4'),
                         ('key2', 'value2'), ('key3', 'value3')])
        in Python 3.12:
            OrderedDict({('key1', 'value1'), ('key4', 'value4'),
                         ('key2', 'value2'), ('key3', 'value3')})
'''
from collections import OrderedDict
from typing import OrderedDict as ODType


def change_dict_order(ordered_dict: ODType) -> ODType:
    """
    Change the order of elements in an OrderedDict according to a specified
    rule.

    Args:
        ordered_dict: The OrderedDict whose order needs to be changed.

    Returns:
        An OrderedDict with elements reordered according to the specified rule.
    """
    new_dict_elements = []

    while len(ordered_dict) > 0:
        rule = len(ordered_dict) % 2 != 0   # True if length is odd, False if even
        current_element = ordered_dict.popitem(last=rule)
        new_dict_elements.append(current_element)

    return OrderedDict(new_dict_elements)


data = OrderedDict({'Name': 'Брусника', 'IsNetObject': 'да',
                    'OperatingCompany': 'Брусника', 'TypeObject': 'кафе',
                    'AdmArea': 'Центральный административный округ', 'District': 'район Арбат',
                    'Address': 'город Москва, переулок Сивцев Вражек, дом 6/2', 'SeatsCount': '10'})
print(change_dict_order(data))
