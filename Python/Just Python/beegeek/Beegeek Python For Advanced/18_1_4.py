'''
TODO:   A text file is available to you "words.txt " with words 
        separated by a space. 

        Write a program that finds and outputs the longest words of this 
        file without changing their order.

NOTE:   Assume that the executable program and the specified file are in 
        the same folder.
        Consider any group of characters without spaces as a word, even 
        if it includes numbers or punctuation marks.
'''


def read_line_from_file(file_name):
    with open(file_name, 'rt', encoding='utf-8') as given_file:
        content = given_file.readline().rstrip()
        given_file.close()

    return content

given_words = read_line_from_file('words.txt')
words_len_dict = {word: len(word) for word in given_words.split()}

max_len = max(words_len_dict.values())

result = []

for key, item in words_len_dict.items():
    if item == max_len:
        result.append(key)

print(*result, sep='\n')