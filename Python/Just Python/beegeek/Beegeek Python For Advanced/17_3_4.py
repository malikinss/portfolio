'''
TODO:   A text file is available to you "numbers.txt" , each line of 
        which can contain one or more integers separated by one or 
        more spaces.

        Write a program that calculates the sum of the numbers in each
        row and displays this amount on the screen (for each row, the sum 
        of the numbers in this row is displayed)

NOTE:   Assume that the executable program and the specified file are in 
        the same folder.
'''


def get_data_from_file(file_name):
    with open(file_name, 'rt', encoding='utf-8') as given_file: # open file for text reading
        content = [row_from_file.rstrip() for row_from_file in given_file.readlines()] # get list of rows from file
        given_file.close() # free memmory

    return content

def get_sum_per_row(data):
    sum_list = []

    for row in data:
        numbers = [int(number) for number in row.split()]
        sum_list.append(sum(numbers))
    
    return sum_list


data = get_data_from_file('numbers.txt')
print(*get_sum_per_row(data), sep='\n')
