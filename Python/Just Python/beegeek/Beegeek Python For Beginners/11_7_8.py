'''
The input to the program is a string of text. Write a list expression program that prints all the numeric characters of a given string.
'''


s = input()
print(*(i for i in s if i.isdigit()), sep="")