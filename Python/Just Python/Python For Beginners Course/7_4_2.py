""" 
Task: The input to the program is a sequence of words, 
each word on a separate line. 
The end of the sequence is the word "END" or "end" (capital 
or small letters, no quotes). 
At the same time, the words “END” and “end” themselves are not 
included in the sequence, only symbolizing its end. 
Write a program that prints the terms of a given sequence.
"""

given_word = input()

keyword_1 = 'END'
keyword_2 = 'end'

while given_word != keyword_1 and given_word != keyword_2:
    print(given_word)
    given_word = input()    