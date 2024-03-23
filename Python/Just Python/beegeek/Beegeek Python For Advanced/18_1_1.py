'''
TODO:   The program is given a line of text with the name of the text file as input. 
        Write a program to display the number of lines of this file.

NOTE:   Assume that the executable program and the specified file are in 
        the same folder.
'''


def read_data_from_file(file_name):
    with open(file_name, 'rt', encoding='utf-8') as given_file:  # open file for text reading
        content = [line.rstrip() for line in given_file.readlines()]  # get list of rows from file
        given_file.close()  # free memmory

    return content

print(len(read_data_from_file(input())))