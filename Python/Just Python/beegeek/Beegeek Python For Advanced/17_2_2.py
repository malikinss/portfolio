'''
TODO:   The input to the program is a string with the name of a text file. 
        Write a program that displays its penultimate line.

NOTE:   Assume that the executable program and the specified file are in the same folder.
        It is guaranteed that the file contains at least two lines.
'''

def get_data_from_file(file_name):
    given_file = open(file_name, 'rt') # open file for text reading
    content = [row_from_file.rstrip() for row_from_file in given_file.readlines()] # get list of rows from file
    given_file.close() # free memmory

    return content

def get_the_penultimate_line(data):
    return data[-2]

data = get_data_from_file(input())

print(get_the_penultimate_line(data))
