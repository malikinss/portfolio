'''
NOTE:   One day, Jacques Fresco was asked:
        - "If you're so smart, why aren't you rich?"

        Jacques did not answer such a provocative question, instead he asked the questioner a riddle:

        - "There were colorful goats. How much?"
        - "How much of what?"
        - "How many of them make up more than 7% of the total number of goats?"

TODO:   A text file is available to you "goats.txt " in the first line  
        of which the word COLORS is written, then there is a list of all possible colors of goats. 
        
        Then there is a line with the word GOATS, and then directly the enumeration of goats of different colors. 
        
        The list of goats includes only the lines from the first list.

        Write a file creation program "answer.txt " and the output of a list of goats that satisfy the condition of the riddle from Jacques Fresco.

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

def get_availible_colours(data):
    colours = {}
    id_counter = 0

    while data[id_counter] != 'GOATS':
        id_counter += 1

        if 'COLOURS' == data[id_counter]:
            continue
        elif data[id_counter] not in colours.keys():
                colours[data[id_counter]] = 0

    return colours

def fill_goat_colours_percentage(counter, goats_list):
    total_goats = len(goats_list)

    for colour in counter.keys():
        goats_per_colour = goats_list.count(colour)
        goats_per_colour_percentage = goats_per_colour / (total_goats / 100)
        counter[colour] = goats_per_colour_percentage

    return counter

def get_goats_list(data):
    goats = []
    start_id = data.index('GOATS') + 1

    for row_id in range(start_id, len(data)):
         goats.append(data[row_id])

    return goats

def get_goats_with_specific_percentage(goats_percentage, specific_percent):
    goats = []

    for goat, percent in goats_percentage.items():
        if percent > specific_percent:
            goats.append(goat)

    goats = sorted(goats)
    
    return goats

def Jacques_Fresco_task(data):
    answer_list = []
    goat_colours_percentage = get_availible_colours(data)
    given_goats_list = get_goats_list(data)
    
    goat_colours_percentage = fill_goat_colours_percentage(goat_colours_percentage, given_goats_list)

    answer_list = get_goats_with_specific_percentage(goat_colours_percentage, 7)

    return answer_list


readen_data = read_data_from_file('goats.txt')
jacques_fresco_answer = Jacques_Fresco_task(readen_data)
data_to_write = convert_list_to_write_format(jacques_fresco_answer)

write_data_to_file('answer.txt', data_to_write)