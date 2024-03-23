'''
TODO:   A text file is available to you "text.txt" with one line of text. 
        Write a program that displays this line in reverse order.

NOTE:   Assume that the executable program and the specified file are in the same folder.
'''


def get_data_from_file(file_name):
    with open(file_name, 'rt', encoding='utf-8') as given_file: # open file for text reading
        content = [row_from_file.rstrip() for row_from_file in given_file.readlines()] # get list of rows from file
        given_file.close() # free memmory

    return content

data = get_data_from_file('text.txt')
reversed_data = data[0][::-1]

print(reversed_data)
