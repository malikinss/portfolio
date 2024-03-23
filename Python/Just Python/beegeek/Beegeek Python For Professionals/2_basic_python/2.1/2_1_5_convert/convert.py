'''
TODO:   
        Implement the convert() function, which takes one argument:
            string — an arbitrary string

        The function should return a string:
            - completely in lowercase if there are more lowercase letters in this line
            - fully uppercase if there are more uppercase letters in this line
            - completely in lowercase if the number of uppercase and lowercase letters in this line is the same

NOTE:   
        String characters that are not letters should be ignored.
'''

def convert(given_string):
    converted_string = ''

    lower_upper_counter = {'lower': 0, 'upper': 0}

    for current_character in given_string:
        if current_character.islower():
            lower_upper_counter['lower'] += 1
        elif current_character.isupper():
            lower_upper_counter['upper'] += 1

    if lower_upper_counter['lower'] >= lower_upper_counter['upper']:
        converted_string = given_string.lower()         
    else:
        converted_string = given_string.upper()

    return converted_string   