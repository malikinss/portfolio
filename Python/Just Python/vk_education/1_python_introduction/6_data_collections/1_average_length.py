'''
TODO:   
        Write a program that will read a string from standard input.

        We need to break the line into words; a word will be considered a sequence of characters other than spaces (that is, punctuation marks will be included in words). 
        
        Next, you need to calculate and display the average number of characters in the words of this text. 
        
        Accuracy is checked to the 2nd decimal place (accuracy +-0.01).

INPUT:
        string

OUTPUT:
        float
'''


words = input().split()
total_characters = sum(map(len, words))
average_length = total_characters/len(words) if words else 0

print(round(average_length, 2))