'''
TODO:  
        Implement a filter_string() function that takes a string and a character as input, and returns a new string with the given character removed in all its positions. 
        
        Avoid using built-in string manipulation methods in your solution.
'''

def filter_string(text, char_to_remove):
    text_runner = 0
    new_text = ''

    while text_runner < len(text):
        cur_char = text[text_runner]
        text_runner += 1

        if cur_char == char_to_remove:    
            continue
        
        new_text += cur_char

    return new_text

def filter_string2(text, char_to_remove):
    filtered_chars = []

    for char in text:
        if char != char_to_remove:
            filtered_chars.append(char)

    return ''.join(filtered_chars)

def filter_string3(text, char_to_remove):
    new_text = ''

    for text_runner in range(len(text)):
        cur_char = text[text_runner]

        if cur_char.lower() == char_to_remove.lower():    
            continue
        
        new_text += cur_char

    return new_text

text = 'If I look back I am lost'
print(filter_string(text, 'w'))