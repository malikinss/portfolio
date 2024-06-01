'''
TODO:
        You have access to the csv file grades.csv, which has the
        following contents:
            name;grade
            Timur;100
            Ruslan;97

        Below is a program that should open this file and output the
        contents of each line as a list.

        There is an error in the program, so it outputs:
            ['n']
            ['a']
            ['m']
            ['e']
            ['', '']
            ['g']
            ['r']
            ['a']
            ['d']
            ['e']
            []
            ['T']
            ...

        Find and correct it so that the program outputs the lines:
            ['name', 'grade']
            ['Timur', '100']
            ['Ruslan', '97']
'''

import csv

with open('grades.csv', encoding='utf-8') as csv_file:
    # read the file contents
    # text = csv_file.read()
    # create a reader object and specify the symbol as a separator;
    rows = csv.reader(csv_file, delimiter=';')

    # output each line
    for row in rows:
        print(row)
