'''
TODO:   You have access to a text file numbers.txt consisting of two lines, each of which contains an integer. 
        Write a program that displays the sum of these numbers.

NOTE:   Assume that the executable program and the specified file are in the same folder.
'''


def get_data_from_file(file_name):
    given_file = open(file_name, 'rt', encoding='utf-8') # open file for text reading
    content = [row_from_file.rstrip() for row_from_file in given_file.readlines()] # get list of rows from file
    given_file.close() # free memmory

    return content

def get_sum_of_data(data):
    sum_of_data = sum(map(int, data))

    return sum_of_data

data = get_data_from_file('numbers.txt')

print(get_sum_of_data(data))
