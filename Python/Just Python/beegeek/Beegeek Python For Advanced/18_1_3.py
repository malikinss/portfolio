'''
TODO:   A text file is available to you "grades.txt ", containing the
        student's grades for three tests in each of the trimesters. 

        The lines of the file have the form: "last name evaluation_1 evaluation_2 evaluation_3"

        Write a program to count the number of students who have passed all three tests. 

        The test is considered passed if the number of points on it is not less than 65.

NOTE:   Assume that the executable program and the specified file are in 
        the same folder.
'''


def read_data_from_file(file_name):
    with open(file_name, 'rt', encoding='utf-8') as given_file:  # open file for text reading
        content = [line.rstrip() for line in given_file.readlines()]  # get list of rows from file
        given_file.close()  # free memmory

    return content

def get_values_int_list(values_str_list):
    values = list(map(int,values_str_list))
    
    return values

def get_data_as_dict(data):
    new_data = []

    for row in data:
        row = row.split()
        
        key = row[0]
        value = get_values_int_list(row[1:])

        new_data.append([key, value])

    return new_data

def is_good_grade(grade):
    return grade >= 65

def map_good_grades(grades):
    return list(map(is_good_grade, grades))

def all_tests_good(grades):
    return all(map_good_grades(grades))

def get_students_with_all_tests_good(data):
    new_data = []

    for record in data:
        student = record[0]
        tests = record[1]

        if all_tests_good(tests):
            new_data.append(student)

    return new_data

data = get_data_as_dict(read_data_from_file('grades.txt'))
result = get_students_with_all_tests_good(data)

#print(*result, sep='\n')
print(len(result))