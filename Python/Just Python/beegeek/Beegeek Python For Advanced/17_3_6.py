'''
TODO:   A text file is available to you "file.txt" , typed in Latin. 
        Write a program that outputs the number of letters of the Latin alphabet, words and strings. 
        Print the three found numbers in the format given in the example.

NOTE:   Assume that the executable program and the specified file are in 
        the same folder.
'''

from string import ascii_letters

def get_output_message(letters_number, words_number, lines_number):
    return (f"Input file contains:\n{letters_number} letters\n{words_number} words\n{lines_number} lines")

def get_data_from_file(file_name):
    with open(file_name, 'rt', encoding='utf-8') as given_file: # open file for text reading
        content = [row_from_file.rstrip() for row_from_file in given_file.readlines()] # get list of rows from file
        given_file.close() # free memmory

    return content

def get_words_number(data):
    total_words = 0

    for row in data:
        total_words += len(row.split())

    return total_words    

def get_letters_number(data):
    total_letters = 0

    for row in data:
        for character in row:
            if character in ascii_letters:
                total_letters += 1

    return total_letters

def get_lines_number(data):
    return len(data)


data = get_data_from_file('file.txt')

letters_number = get_letters_number(data)
words_number = get_words_number(data)
lines_number = get_lines_number(data)

print(get_output_message(letters_number, words_number, lines_number))
