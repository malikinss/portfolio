'''
TODO: A pangram is a phrase containing all the letters of the alphabet. 
Typically, pangrams are used to present fonts so that all glyphs can be considered in one phrase.
Write a function is_pangram(text) that takes a string of English text as an argument and returns True if the text is a pangram and False otherwise.
NOTE: It is guaranteed that the entered string contains only English letters and spaces.
'''


def is_pangram(text):
    text = text.lower()
    for i in range(ord("a"), ord("z") + 1):
        if chr(i) not in text:
            return False
    
    return True


text = input()

print(is_pangram(text))