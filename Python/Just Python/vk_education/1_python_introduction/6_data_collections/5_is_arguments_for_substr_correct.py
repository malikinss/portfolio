'''
TODO:  
        Implement a predicate function is_arguments_for_substr_correct() that takes three arguments:
            - string;
            - index from which to start extraction;
            - length of the extracted substring.

        The function returns False if at least one of the conditions is true:
            - Negative length of the substring to be extracted.
            - Negative specified index.
            - The specified index extends beyond the boundary of the entire row.
            - The length of the substring plus the given index exceeds the boundary of the entire string.

        Otherwise, the function returns True.
'''

def is_arguments_for_substr_correct(given_string, start_index, sub_string_len):
    end_index = start_index + sub_string_len

    negative_sub_string_len = sub_string_len < 0
    negative_start_index = start_index < 0

    out_of_range_start_index = (start_index > len(given_string) - 1)
    out_of_range_sub_string = (end_index > len(given_string))
    
    negative_data_cases = negative_sub_string_len or negative_start_index
    out_of_range_cases = out_of_range_start_index or out_of_range_sub_string

    if negative_data_cases or out_of_range_cases:
        return False
    return True

string = 'Sansa Stark'
end = len(string) - 1
print(is_arguments_for_substr_correct(string, end, 1))