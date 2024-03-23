'''
TODO: It is necessary to write a program that implements the algorithm for writing this song. 
The algorithm displays the next letter in alphabetical order at the end of the sentence if it occurs in a line of text, and displays the next line without this letter.

NOTE: If there are no Tails, then you need to output the number 0.
'''

word = input() + ' banned the letter'
alpha = [chr(i) for i in range(1072, 1104)]

for letter in alpha:

    if letter in word:
        print(word, letter)
        word = word.replace(letter, '').replace('  ', ' ').strip()