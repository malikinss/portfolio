""" 
Task: The input to the program is a string containing English text. Write a program that counts the total number of articles: 'a', 'an', 'the'.
"""

given_string = input()
counter = 0

list_1 = ['a', 'an', 'the']
list_2 = given_string.lower().split()

for i in range(len(list_1)):
    counter += list_2.count(list_1[i])

print('total number of articles:', counter) 