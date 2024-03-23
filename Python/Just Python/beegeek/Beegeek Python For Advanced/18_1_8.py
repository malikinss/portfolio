'''
TODO:   When writing your own functions, it is recommended to describe the purpose of the function, its parameters and the return value in the comments. 

Programmers often postpone writing such comments until the last, and then completely forget about them.

The input to the program is a string of text with the name of the text file in which the Python code is written. 

Write a program that displays the names of all functions for which there is no explanatory comment. 

Let's assume that any line starting with the word def and a space is the beginning of the function definition. 

The function contains a comment if the first character of the previous line is #.

NOTE:   Consider that the executable program and the specified files are 
        in the same folder.


'''
def read_data_from_file(file_name):
    with open(file_name, 'rt', encoding='utf-8') as given_file:
        content = [line.rstrip() for line in given_file.readlines()]
        given_file.close()

    return content

given_code = read_data_from_file(input())

output_list = []

for line_number in range(1, len(given_code)):
    line = given_code[line_number]
    prev_line = given_code[line_number - 1]

    if line.startswith('def ') and prev_line.startswith('# ') != True:
        function_name = line[4:line.index('(')]
        output_list.append(function_name)
    elif line_number == 1 and prev_line.startswith('def '):    
        function_name = prev_line[4:prev_line.index('(')]
        output_list.append(function_name)

if len(output_list) == 0:
    print('Best Programming Team')
else:
    print(*output_list, sep='\n')