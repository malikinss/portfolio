""" 
Task: The input to the program is a sequence of words, each word 
on a separate line. 
The end of the sequence is the word "END" (without quotes). 
At the same time, the word "END" itself is not included in the sequence, 
only symbolizing its end. 
Write a program that prints the terms of a given sequence.
"""

given_word = input()

while given_word != 'END':
    print(given_word)
    given_word = input()