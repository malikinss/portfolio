'''
TODO: BEEGEEK has finally opened its own bank, which uses special ATMs with an unusual password.

A valid BEEGEEK bank password is a:b:c, where a, b and c are natural numbers. 
Since the founder of BEEGEEK is a math fanatic, he decided:

number a - must be a palindrome;
number b - must be prime;
number c - must be even.

Write a function is_valid_password(password) that takes the string value of password as an argument and returns True if the password is a valid BEEGEEK bank password and False otherwise.
'''


def is_palindrome(text):
    symbols = [' ', ',', '.', '!', '?', '-']
    
    for c in symbols:
        text = text.replace(c, '')
    
    text = text.lower()
    
    return text == text[::-1]


def is_even(num):
    return num % 2 == 0


def is_prime(num):
    lst = [i for i in range(1, num + 1) if num % i == 0]
    
    if len(lst) == 2:
        return True
    else:
        return False



def is_valid_password(password):
    seq = password.split(":")
    
    if len(seq) == 3:
        seq = [int(el) for el in seq]
        a, b, c = seq[0], seq[1], seq[2]
        
        return is_palindrome(str(a)) and is_prime(b) and is_even(c)
    
    return False



psw = input()

print(is_valid_password(psw))