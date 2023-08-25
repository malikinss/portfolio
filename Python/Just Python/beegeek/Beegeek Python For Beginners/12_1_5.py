'''
The input to the program is a string of text. 
Write a program using a list expression that finds the length of the longest word.
'''
given_string = input().split()

print(max([len(word) for word in given_string]))