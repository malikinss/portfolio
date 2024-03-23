'''
TODO:   
        Write a program that will read a string from standard input and print to standard output whether the string is “correct”. 
        
        A string is considered correct if it contains the Latin letter “a” or “o”, but does not contain the letters “i” and “e”. 
        
        The string contains only lowercase Latin letters.

INPUT:
        string

OUTPUT:
        True/False
'''

def is_correct_string(given_string):

    check_string = given_string.lower()
    
    condition_1 = 'a' in check_string
    condition_2 = 'o' in check_string
    condition_3 = 'i' not in check_string
    condition_4 = 'e' not in check_string

    condition_5 = condition_1 or condition_2
    condition_6 = condition_3 and condition_4

    correct_string = condition_5 and condition_6

    return correct_string

print(is_correct_string(input()))