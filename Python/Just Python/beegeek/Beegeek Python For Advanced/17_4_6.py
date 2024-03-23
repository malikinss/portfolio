'''
TODO:   The program is supplied with a natural number of n and n lines 
        with file names.

        Write a program that creates a file output.txt and outputs the contents of all files to it without changing their order.

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

def get_file_names(files_number):
    file_names_list = []

    for i in range(files_number):
        file_name = input()
        file_names_list.append(file_name)

    return file_names_list


def concat_files(files_number):
    file_names = get_file_names(files_number)

    data_to_write = []

    for file_name in file_names:
        readen_data = read_data_from_file(file_name)
        readen_data = convert_list_to_write_format(readen_data)
        
        if len(readen_data) > 0:
            readen_data[-1] = readen_data[-1].rstrip()

        #print(readen_data)
        data_to_write.extend(readen_data)

    return data_to_write    


result_data_to_write = concat_files(int(input()))

write_data_to_file('output.txt', result_data_to_write)