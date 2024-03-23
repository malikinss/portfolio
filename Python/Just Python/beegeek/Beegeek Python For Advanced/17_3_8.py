'''
TODO:   A text file is available to you "population.txt " with the 
        names of countries and their populations separated by the tab character '\t'.

        Write a program that outputs all countries whose names begin with the letter 'G', whose population is more than
        500,000 people, without changing their order.

NOTE:   Assume that the executable program and the specified file are in 
        the same folder.
'''

from random import choice

def get_data_from_file(file_name):
    with open(file_name, 'rt', encoding='utf-8') as given_file: # open file for text reading
        content = [row_from_file.rstrip() for row_from_file in given_file.readlines()] # get list of rows from file
        given_file.close() # free memmory

    return content

def get_correct_data(data):
    new_data = []

    for row in data:
        new_row = row.split('\t')
        new_data.append(new_row)

    return new_data

data = get_data_from_file('population.txt')
data = get_correct_data(data)

filtered_data = list(filter(lambda row: row if row[0].startswith('G') and int(row[1]) > 500_000 else False, data))

countries = [row[0] for row in filtered_data]


print(*countries, sep='\n')
