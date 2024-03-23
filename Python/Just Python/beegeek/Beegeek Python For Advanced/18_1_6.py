'''
TODO:   The program is given a line of text with the name of the text 
        file as input. 

        Write a program that displays the contents of this file, but with the replacement of all forbidden words with asterisks * (the number of asterisks is equal to the number of letters in the word).

        Forbidden words separated by a space character are stored in a text file forbidden_words.txt . 

        It is guaranteed that all words in this file are written in lowercase.

NOTE:   Your program should replace the forbidden words wherever they 
        occur, even if they occur in the middle of another word.

        The program must replace forbidden words regardless of their
        case. 

        For example, if the file forbidden_words.txt contains the
        forbidden word exam, then the words exam, Exam, ExaM, EXAM and
        the like should be replaced with ****.
'''

def get_forbidden_words():
    with open('forbidden_words.txt', 'rt', encoding='utf-8') as file:
        words = file.read().split()
        
        return words

def get_index_of_forbidden_word(line, word):
    return line.lower().index(word)


def replace_forbidden_word(word, line, index):
    return line[:index] + '*' * len(word) + line[index+len(word):]

def get_converted_string(words, line):
    for word in words:
        while word in line.lower():
            index = get_index_of_forbidden_word(line, word)
            line = replace_forbidden_word(word, line, index)

    return line        

def task():
    with open(input(), 'rt', encoding='utf-8') as text_file:
        forbidden_words = get_forbidden_words()

        for line in text_file:
            converted_line = get_converted_string(forbidden_words, line)
            print(converted_line.strip())

task()            
