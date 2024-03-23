'''
TODO:   Write a program that writes to a text file "random.txt" 25 
        random numbers in the range from 111 to 777 (inclusive), each 
        with a new line.

NOTE:   Assume that the executable program and the specified file are in 
        the same folder.
'''

from random import sample

def write_data_to_file(file_name, data):
    with open(file_name, 'w', encoding='utf-8') as file:
        file.writelines(data)

def get_list_of_random_numbers(range_start, range_end, quantity):
    return sample(range(range_start, range_end), quantity)

def convert_list_to_write_format(data):
    converted_data = list(map(lambda x: str(x)+'\n', data))
    return converted_data

random_numbers = get_list_of_random_numbers(111, 777, quantity=25)
data_to_write = convert_list_to_write_format(random_numbers)

write_data_to_file('random.txt', data_to_write)