'''
TODO:   Two text files are available to you "first_names.txt" and 
        "last_names.txt", one with names, the other with surnames.

        Write a program that uses the random module to create
        3 random pairs of first name + last name, and then outputs 
        them, each on a separate line.

NOTE:   Assume that the executable program and the specified file are in 
        the same folder.
'''

from random import choice

def get_data_from_file(file_name):
    with open(file_name, 'rt', encoding='utf-8') as given_file: # open file for text reading
        content = [row_from_file.rstrip() for row_from_file in given_file.readlines()] # get list of rows from file
        given_file.close() # free memmory

    return content

def get_one_random_person(last_names, first_names):
    random_last_name = choice(last_names)
    random_first_name = choice(first_names)

    person = random_first_name + ' ' + random_last_name

    return person

def get_random_persons(last_names, first_names, persons_number):
    random_persons = []

    for _ in range(persons_number):
        person = get_one_random_person(last_names, first_names)
        random_persons.append(person)

    return random_persons


last_names = get_data_from_file('last_names.txt')
first_names = get_data_from_file('first_names.txt')

output_list = get_random_persons(last_names, first_names, persons_number=3)

print(*output_list, sep='\n')
