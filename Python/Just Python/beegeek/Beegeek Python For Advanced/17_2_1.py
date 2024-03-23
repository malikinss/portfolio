'''
TODO:   The input to the program is a string with the name of a text file. 
        Write a program that displays its contents on the screen.

NOTE:   Assume that the executable program and the specified file are in the same folder.
'''

def get_data_from_file(file_name):
    given_file = open(file_name, 'rt') # open file for text reading
    content = [row_from_file.rstrip() for row_from_file in given_file.readlines()] # get list of rows from file
    given_file.close() # free memmory

    return content

print(*get_data_from_file(input()), sep='\n')
