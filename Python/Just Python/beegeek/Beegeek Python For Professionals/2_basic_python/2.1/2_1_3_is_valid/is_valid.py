'''
TODO:   We will assume that the PIN code is correct if it meets the following conditions:

            - consists of 4, 5 or 6 characters
            - consists only of digits (0-9)
            - does not contain spaces

        Implement the is_valid() function, which takes one argument:

            string — an arbitrary string

        The function should return True if the string is a valid PIN, or False otherwise.

NOTE:   If an empty string is passed to the function, the function must return False.
'''

def is_valid(string):
    flags = {}

    flags['length'] = (len(string) in range(4,7))
    flags['digits'] = string.isdigit()
    flags['spaces'] = ' ' not in string

    return all(flags.values())
