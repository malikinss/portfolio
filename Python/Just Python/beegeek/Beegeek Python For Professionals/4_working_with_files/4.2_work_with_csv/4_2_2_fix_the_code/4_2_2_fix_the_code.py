'''
TODO:
        When you try to run the program below, an error occurs.
        Find and fix it so that the program creates a file called
        writing_test.csv that has the following contents:
            first_col,second_col
            value1,value2
'''

import csv

with open('writing_test.csv', 'w', encoding='utf-8') as csv_file:
    # create a writer object and specify the column names
    writer = csv.DictWriter(csv_file, fieldnames=['first_col', 'second_col'])

    # write the first line with column names
    writer.writeheader()

    # write a line with data
    writer.writerows([{'first_col': 'value1', 'second_col': 'value2'}])
