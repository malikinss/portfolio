'''
TODO:
        Calculate and print the number of identical elements in the collections string_1 and string_2.
'''

def  get_set_from_str(given_string):
    return set(given_string.split())

def count_identical_elements(string_1, string_2):
    set_1 = get_set_from_str(string_1)
    set_2 = get_set_from_str(string_2)

    same_elems = set_1.intersection(set_2)
    
    return len(same_elems)

string_1 = '100 13 2 143 12 3 55 4 64 18 56'
string_2 = '234 2 56 432 3 100 12 99 43 18 31 64'

print(count_identical_elements(string_1, string_2))