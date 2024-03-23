'''
TODO:   The program is given a line of text with the name of the text 
        file as input. 

        Write a program that displays the latest 10 lines of this file.

NOTE:   Assume that the executable program and the specified file are in 
        the same folder.
        If the number of lines in the file is less than 10, it is 
        necessary to print the entire contents of the file.
'''


def read_data_from_file(file_name):
    with open(file_name, 'rt', encoding='utf-8') as given_file:
        content = [line.rstrip() for line in given_file.readlines()]
        given_file.close()

    return content

data = read_data_from_file(input())

if 10 > len(data):
    print(*data, sep='\n')
else:
    print(*data[-10:], sep='\n')    