""" 
Task: The input to the program is a sequence of words, 
each word on a separate line. 
The end of the sequence is one of three words: 
“stop”, “enough”, “sufficiently” (in small letters, without quotes). 
These words themselves are not included in the sequence, 
only symbolizing its end. 
Write a program that prints the total number of terms in a given sequence.
"""

given_word = input()

counter = 1

keyword_1 = 'stop'
keyword_2 = 'enough'
keyword_3 = 'sufficiently'

while given_word != keyword_1 and given_word != keyword_2 and given_word != keyword_3:
    given_word = input()
    counter += 1

print(counter-1)