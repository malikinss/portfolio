'''
TODO: 
        Anton received in response from the server a list of client ids in the form of a string, where the ids are separated by spaces. 
        
        Its task is to remove duplicates and sort the list of ids in ascending order.

        Write a program that will help Anton generate such lists. 
        
        If a duplicate id is found in the list, the program should display the message “Duplicate id <id_value> found” in the terminal.
'''

def  get_int_list_from_collection(collection):
    return  list(map(int, collection.split()))

def display_message_if_duplicate(id_value):
    print(f'Duplicate id {id_value} found')

def remove_all_duplicates_and_sort(ids_list):
    id_set = set()

    for id in ids_list:
        if id in id_set:
            display_message_if_duplicate(id)
        id_set.add(id)
    
    return sorted(id_set)

id_string = '32 48 2 6 14 58 2 88 9 14 123 48 3 17 42 42 7'
id_list = get_int_list_from_collection(id_string)
id_list = remove_all_duplicates_and_sort(id_list)

print(id_list)