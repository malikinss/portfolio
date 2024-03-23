'''
TODO:   You have access to a text file "lines.txt" consisting of several lines. 
        Write a program that prints a random line from this file to the screen.

NOTE:   Assume that the executable program and the specified file are in the same folder.
        It is guaranteed that the file contains at least one line.
'''


from random import randint


def get_data_from_file(file_name):
    given_file = open(file_name, 'rt', encoding='utf-8') # open file for text reading
    content = [row_from_file.rstrip() for row_from_file in given_file.readlines()] # get list of rows from file
    given_file.close() # free memmory

    return content

def get_random_line(data):
    rows_number = len(data)
    random_row_number = randint(0, rows_number)

    return data[random_row_number]

data = get_data_from_file('lines.txt')

print(get_random_line(data))
