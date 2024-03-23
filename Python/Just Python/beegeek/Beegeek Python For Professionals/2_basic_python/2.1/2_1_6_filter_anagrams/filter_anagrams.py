'''
TODO:   
        Anagrams are words that consist of identical letters. 
        Implement the filter_anagrams() function, which takes two arguments in the following order:

            word — lowercase word
            words — a list of words in lowercase

        The function should return a list, the elements of which are words from the words list, which represent an anagram of the word word. 
        If the words list is empty or does not contain anagrams, the function should return an empty list.

NOTE:   
        The words in the list returned by the function must be in their original order. 
        Consider the word to be an anagram of itself.
'''

def count_each_letter(word):
    letters_counter = {}

    for letter in word:
        if letter not in letters_counter.keys():
            letters_counter[letter] = 1
        else:
            letters_counter[letter] += 1

    return letters_counter            

def filter_anagrams(word, words):
    filtered_words = []
    compare_word_letters = count_each_letter(word)

    for element in words:
        if compare_word_letters == count_each_letter(element):
            filtered_words.append(element)

    return filtered_words