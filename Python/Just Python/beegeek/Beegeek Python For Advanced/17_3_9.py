'''
TODO:   The CSV file data.csv is available to you, containing
        information in csv format. 
        Write the read_csv function to read data from this file. 
        It should return a list of dictionaries, interpreting the first 
        line as the names of the keys, and each subsequent line as the 
        values of these keys.

NOTE:   Assume that the executable program and the specified file are in 
        the same folder.
'''

def get_data_from_file(file_name):
    with open(file_name, 'rt', encoding='utf-8') as given_file: # open file for text reading
        content = [line.rstrip() for line in given_file.readlines()] # get list of rows from file
        given_file.close() # free memmory

    return content

def get_keys_from(data):
    keys = data[0].split(',')
    
    return keys

def get_values_from(data, value_id):
    values = data[value_id].split(',')
    
    return values

def read_csv():
    csv_dict = []

    data = get_data_from_file('data.csv')
    number_of_records = len(data) # include first row (keys for dict)

    keys = get_keys_from(data)

    for record_id in range(1, number_of_records):
        record = {}

        values = get_values_from(data, record_id)
        
        for id in range(len(values)):
            record[keys[id]] = values[id]

        csv_dict.append(record)

    return csv_dict    


print(read_csv())
