'''
TODO:   A text file is available to you "class_scores.txt " with grades 
        for the final test on lines like: 
        - surname assessment (surname and assessment are separated by a space). 
        The score is an integer from 0 to 100 inclusive.

        Write a program to add 5 points for each test result and output of surnames and new test results to a file "new_scores.txt ".

NOTE:   Assume that the executable program and the specified file are in 
        the same folder.
'''


def read_data_from_file(file_name):
    with open(file_name, 'rt', encoding='utf-8') as given_file:  # open file for text reading
        content = [line.rstrip() for line in given_file.readlines()]  # get list of rows from file
        given_file.close()  # free memmory

    return content

def write_data_to_file(file_name, data):
    with open(file_name, 'w', encoding='utf-8') as file:
        file.writelines(data)

def convert_list_to_write_format(data):
    converted_data = list(map(lambda x: str(x)+'\n', data))
    return converted_data

def add_scores(data, score_to_add):
    result = []

    for row in data:
        new_row = row.split()
        new_score = int(new_row[1]) + score_to_add
        
        if new_score > 100:
            new_score = 100

        new_row = new_row[0] + ' ' + str(new_score)
        
        result.append(new_row)

    return result     

readen_data = read_data_from_file('class_scores.txt')
data_to_write = convert_list_to_write_format(add_scores(readen_data, 5))

write_data_to_file('new_scores.txt', data_to_write)