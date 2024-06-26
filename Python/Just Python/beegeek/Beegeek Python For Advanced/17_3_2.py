'''
TODO:   A text file is available to you data.txt , which contains lines of text. 
        Write a program that outputs all the lines of this file in reverse order: first the last one, then the penultimate one, etc.

NOTE:   Assume that the executable program and the specified file are in the same folder.
'''


def get_data_from_file(file_name):
    with open(file_name, 'rt', encoding='utf-8') as given_file: # open file for text reading
        content = [row_from_file.rstrip() for row_from_file in given_file.readlines()] # get list of rows from file
        given_file.close() # free memmory

    return content

data = get_data_from_file('data.txt')
reversed_rows_order = data[::-1]

print(*reversed_rows_order, sep='\n')
