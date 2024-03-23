'''
TODO:   
        You have access to the text file files.txt, which contains information about the files.
        
        Each line of the file contains three values, separated by a space character - the file name, its size (integer) and units of measurement:

            cant-help-myself.mp3 7 MB
            keep-yourself-alive.mp3 6 MB
            bones.mp3 5 MB
            ...

        Write a program that groups these files by extension, determining the total size of the files in each group, and displays the resulting groups of files, indicating the total size for each.
        
        Groups must be arranged in lexicographic order of extension names, files in groups - in lexicographic order of their names.        

NOTE:   
        For example, if the files.txt file looked like:

            input.txt 3000 B
            scratch.zip 300 MB
            output.txt 1 KB
            temp.txt 4 KB
            boy.bmp 2000 KB
            mario.bmp 1 MB
            data.zip 900 MB

        then the program should output:

            boy.bmp
            mario.bmp
            ----------
            Summary: 3 MB

            input.txt
            output.txt
            temp.txt
            ----------
            Summary: 8 KB

            data.zip
            scratch.zip
            ----------
            Summary: 1 GB

        where Summary is the total size of the group files.

        It is guaranteed that all file names contain the extension.

        The total size of the group's files is recorded in the largest (maximum possible) units of measurement, rounded to the nearest whole unit.
        
        In other words, you should first determine the total volume of all files in a group, say, in bytes, and then convert the resulting value into the largest (maximum possible) units of measurement.
        
        Convertion examples:
            1023 B -> 1023 B
            1300 B -> 1 KB
            1900 B -> 2 KB

        The values of units of measurement are the same as those accepted in computer science:
            1 KB = 1024 B
            1 MB = 1024 KB
            1 GB = 1024 MB
'''

def read_data_from_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as given_file:
        return [line.rstrip() for line in given_file.readlines()]

def get_file_info(record):
    filename, size_str, unit = record.split()
    filename_value, extension_value = filename.split('.')

    return { 'filename': filename_value, 
            'extension': extension_value, 
            'size': int(size_str), 
            'unit': unit}

def get_list_of_files_info(file_to_open):
    return [get_file_info(record) for record in read_data_from_file(file_to_open)]


def unique_values(files, key):
    return sorted({file[key] for file in files})


def filter_files_by_key(key, value, files):
    return list(filter(lambda file: file[key] == value, files))

def get_total_size_for_same_unit_extension(extension, unit, files):
    files_per_extension = filter_files_by_key('extension',extension, files)
    files_per_unit = filter_files_by_key('unit',unit, files_per_extension)

    total = 0
    for file in files_per_unit:
        total += file['size']

    return total

def convert_to_bytes(size, unit='B'):
    unit_conversion = {'B': 1, 'KB': 1024, 'MB': 1024 * 1024, 'GB': 1024 * 1024 * 1024}

    return size * unit_conversion.get(unit, 1)

def convert_bytes_to_chosen_unit(size_in_bytes, unit='B'):
    unit_conversion = {'B': 1, 'KB': 1024, 'MB': 1024 * 1024, 'GB': 1024 * 1024 * 1024}

    return round(size_in_bytes / unit_conversion.get(unit, 1))

def get_bytes_in_diff_units(size_in_bytes, units):
    return {unit: convert_bytes_to_chosen_unit(size_in_bytes, unit) for unit in units}

def get_bytes_in_greater_unit(size, units):
    output_list = [0, 'B'] # first element for value second for unit
    size_translation = get_bytes_in_diff_units(size, units)

    for unit, value in size_translation.items():
        if value == 0:
            continue
        
        output_list[0] = value
        output_list[1] = unit

    return output_list    

def calculate_total_size_for_extension_in_bytes(files, extension, units):
    total_extension_in_bytes = 0
    
    for unit in units:
        total_unit = get_total_size_for_same_unit_extension(extension, unit, files)
        total_unit_in_bytes = convert_to_bytes(total_unit, unit)
        total_extension_in_bytes += total_unit_in_bytes

    return total_extension_in_bytes

def concat_filenames_with_extension(files, extension):
    return sorted([f"{file['filename']}.{extension}" for file in files]) 

def print_result_form(filenames, size_unit_out):
    print(*filenames, sep='\n')
    print('-'*10)
    print('Summary:', *size_unit_out)  
    print()

def group_files_by_extension(extension, files):
    filtered_files = filter_files_by_key('extension', extension, files)
    filenames = concat_filenames_with_extension(filtered_files, extension)

    return filenames

def get_size_in_greater_unit(files, extension):
    existing_units = ['B', 'KB', 'MB', 'GB']

    total_extension_in_bytes = calculate_total_size_for_extension_in_bytes(files, extension, existing_units)
    
    size_unit_out = get_bytes_in_greater_unit(total_extension_in_bytes, existing_units)
    
    return size_unit_out

def group_files_by_extension_and_calculate_total_sizes(files):

    existing_extensions = unique_values(files, key='extension')

    for extension in existing_extensions:
        filenames = group_files_by_extension(extension, files)
        size_unit_out = get_size_in_greater_unit(files, extension)

        print_result_form(filenames, size_unit_out)


file_to_open = "C:/Users/malik/Documents/GitHub/portfolio/Python/Just Python/beegeek/Beegeek Python For Professionals/2.2/9_group_files_by_extension_and_calculate_total_sizes/files.txt"
data = get_list_of_files_info(file_to_open)

print(data)
print('*' * 20)
group_files_by_extension_and_calculate_total_sizes(data)
