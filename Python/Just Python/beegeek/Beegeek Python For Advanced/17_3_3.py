'''
TODO:   A text file is available to you "lines.txt" , which contains lines of text. 
        Write a program that outputs all the longest strings from a file without changing their order.

NOTE:   Assume that the executable program and the specified file are in the same folder.
'''


def get_data_from_file(file_name):
    with open(file_name, 'rt', encoding='utf-8') as given_file: # open file for text reading
        content = [row_from_file.rstrip() for row_from_file in given_file.readlines()] # get list of rows from file
        given_file.close() # free memmory

    return content

def filter_by_length(row):
    return len(row)

data = get_data_from_file('lines.txt')
max_len = len(max(data, key=len))

filtered_data_by_length = list(filter(lambda x: x if len(x) == max_len else False, data))

print(*filtered_data_by_length, sep='\n')
