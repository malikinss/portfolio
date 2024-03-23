'''
TODO:   
        It is necessary to write a program that will read a string from standard input, then convert it to lower case, and also replace the characters “!”, “%”, “#”, “@” with an empty string. 
        
        As a result, you will need to display the number of replaced characters in the first line, and the converted string in the second.     
'''

CHARS_TO_REPLACE = ['!', '%', '#', '@']

given_string = input().lower()

replacement_counter = 0

output_string = ''.join([char for char in given_string if char not in CHARS_TO_REPLACE])


replacement_counter = len(given_string) - len(output_string)

print(replacement_counter)
print(output_string)