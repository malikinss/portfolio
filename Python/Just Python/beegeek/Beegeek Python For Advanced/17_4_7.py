'''
TODO:   A text file is available to you "logfile.txt " with information 
        about the time the user logs in and out of the system. 

        Each line of the file contains three values separated by commas and a space character: 
            -user name
            -entry time
            -exit time 
        
        where the time is indicated in 24 - hour format.

        Write a program that creates a file "output.txt " and outputs to it the names of all users (without changing the order) who have been online for at least an hour.

NOTE:   Assume that the executable program and the specified file are in 
        the same folder.
        Consider that each user has been in the system only once, that is, there are no two lines in the file with the same user.
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

 
def convert_row_to_list(row):
    row_as_list = row.split(', ')

    return row_as_list

def convert_data_to_nested_lists(data):
    new_data = []

    for row in data:
        new_row = convert_row_to_list(row)
        new_data.append(new_row)

    return new_data

def get_time_as_int_list(time):
    return [int(element) for element in time.split(':')]

def convert_hours_in_minutes(hours):
    return hours * 60

def convert_str_time_to_int_min(time):
    hours, minutes = get_time_as_int_list(time)
    total_minutes = convert_hours_in_minutes(hours) + minutes

    return total_minutes

def get_minutes_difference(time_1, time_2):
    minutes_1 = convert_str_time_to_int_min(time_1)
    minutes_2 = convert_str_time_to_int_min(time_2)

    difference_minutes = minutes_2 - minutes_1

    return difference_minutes

def get_time_difference(time_1, time_2):
    time_list = []

    minutes_diff = get_minutes_difference(time_1, time_2)
    
    hours = minutes_diff // 60
    minutes = minutes_diff - (hours * 60)

    time_list.append(hours)
    time_list.append(minutes)

    return time_list

def get_data_with_minutes(data):
    new_data = {}

    data = convert_data_to_nested_lists(data)

    for record in data:
        name = record[0]
        start_time = record[1]
        finish_time = record[2]

        new_data[name] = get_minutes_difference(start_time, finish_time)

    return new_data

def get_users_who_spent_more_than_hour(data):
    users = []
    
    for user, minutes in data.items():
        if minutes >= 60:
            users.append(user)

    return users


readen_data = read_data_from_file('logfile.txt')

user_minutes_dict = get_data_with_minutes(readen_data)
result_data_to_write = get_users_who_spent_more_than_hour(user_minutes_dict)

write_data_to_file('output.txt', convert_list_to_write_format(result_data_to_write))