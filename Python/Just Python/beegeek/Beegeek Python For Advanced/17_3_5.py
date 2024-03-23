'''
TODO:   A text file is available to you "nums.txt" . 
        The file can contain non-negative integers and anything else. 
        Let's call a number a sequence of one or more digits in a row 
        (the number is always non-negative).

        Write a program that calculates the sum of all the numbers 
        written in the file.

NOTE:   Assume that the executable program and the specified file are in 
        the same folder.
'''


def get_data_from_file(file_name):
    with open(file_name, 'rt', encoding='utf-8') as given_file: # open file for text reading
        content = [row_from_file.rstrip() for row_from_file in given_file.readlines()] # get list of rows from file
        given_file.close() # free memmory

    return content

def convert_all_extra_chars_to_space(data):
    new_data = []

    for row in data:
        new_row = ''
        
        for character in row:
            if character.isdigit() != True:
                new_row += ' '
            else:
                new_row += character    

        new_data.append(new_row)

    return new_data
    
def get_all_nums_in(data):
    numbers = []

    for row in data:
        numbers.extend([int(number) for number in row.split() if number.isdigit()])   
    
    return numbers


data = get_data_from_file('nums.txt')
data = convert_all_extra_chars_to_space(data)
nums = get_all_nums_in(data)
print(sum(nums))
