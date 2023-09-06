'''
TODO: Write a function is_password_good(password) that takes the string value password as an argument and returns True if the password is strong and False otherwise.
A password is strong if:
- its length is at least 8 characters;
- it contains at least one capital letter (upper case);
- it contains at least one lowercase letter (lower case);
- it contains at least one digit.
'''


def is_password_good(password):
    upp = [i for i in password if i.isupper()]
    low = [i for i in password if i.islower()]
    dig = [i for i in password if i.isdigit()]
    return all([len(password) >= 8, upp, low, dig])


txt = input()

print(is_password_good(txt))