'''
TODO:   A text file is available to you ledger.txt with the company's 
        sales data for the month. 

        Each line of the file shows how much the customer paid for the
        product, in dollars (an integer).

        Write a program to calculate the total monthly revenue of the
        company.

NOTE:   Assume that the executable program and the specified file are in 
        the same folder.
'''


def read_data_from_file(file_name):
    with open(file_name, 'rt', encoding='utf-8') as given_file:  # open file for text reading
        content = [line.rstrip() for line in given_file.readlines()]  # get list of rows from file
        given_file.close()  # free memmory

    return content

def get_payments_as_int_list(data):
    new_data = []
    
    for element in data:
        new_element = int(element.lstrip('$'))
        new_data.append(new_element)

    return new_data

payments = get_payments_as_int_list(read_data_from_file('ledger.txt'))
total_sum = str(sum(payments))

print('$' + total_sum)