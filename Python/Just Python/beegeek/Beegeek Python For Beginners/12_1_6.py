'''
The input to the program is a string of text. 
Write a list expression program that converts each word of the input text into "youth jargon" according to the following rule:

the first letter of each word is removed and placed at the end of the word;
then the syllable "ki" is added to the end of the word.
'''

given_string = input().split()
print(*[word[1:] + word[0] + "ki" for word in given_string])