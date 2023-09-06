'''
TODO: Write a function is_palindrome(text) that takes the string text as an argument and returns True if the specified text is a palindrome and False otherwise.
'''


def is_palindrome(text):
    symbols = [' ', ',', '.', '!', '?', '-']
    
    for c in symbols:
        text = text.replace(c, '')
    
    text = text.lower()
    
    return text == text[::-1]


txt = input()


print(is_palindrome(txt))