'''
TODO:   A text file is available to you "input.txt" consisting of several lines.
        Write a program to write the contents of this file to a file "output.txt" 
        in the form of a numbered list, where each line is preceded by its number, 
        character ")" and a space. 
        The line numbering should start with "1".

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

def enumerate_data_rows(data):
    enumerated_data = []

    for id, item in enumerate(data, start=1):
        record = str(id) + ') ' + item
        enumerated_data.append(record)

    return enumerated_data


readen_data = enumerate_data_rows(read_data_from_file('input.txt'))
data_to_write = convert_list_to_write_format(readen_data)

write_data_to_file('output.txt', data_to_write)