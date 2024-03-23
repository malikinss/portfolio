'''
TODO:   The text file nums.txt is available to you. 
        The file contains two integers; they can be separated by space and end-of-line characters. 
        Write a program that displays the sum of these numbers.

NOTE:   Assume that the executable program and the specified file are in the same folder.
'''


def get_all_data_from_file(file_name):
    given_file = open(file_name, 'rt', encoding='utf-8') # open file for text reading
    content = given_file.read().split() # get list of rows from file
    given_file.close() # free memmory

    return content

def get_sum_of_data(data):
    sum_of_data = sum(map(int, data))

    return sum_of_data

data = get_all_data_from_file('nums.txt')

print()
print('result =',get_sum_of_data(data))
print()