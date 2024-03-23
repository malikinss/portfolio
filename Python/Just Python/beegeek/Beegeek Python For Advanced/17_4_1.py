'''
TODO:   Write a program that reads a line of text and writes it 
        to a text file output.txt .

NOTE:   Assume that the executable program and the specified file are in 
        the same folder.
'''

def write_data_to_file(file_name, data):
    with open(file_name, 'w', encoding='utf-8') as file:
        file.writelines(data)

given_data = input()
write_data_to_file('output.txt', given_data)