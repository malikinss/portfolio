'''
TODO:   
        Implement the spell() function, which takes an arbitrary number of positional arguments-words and returns a dictionary whose keys are the first letters of the words, and the values are the maximum word lengths for this letter.

NOTE:   
        If no arguments are passed to the function, the function must return an empty dictionary.

        The function should ignore the case of words, while the resulting dictionary should contain exactly letters in lowercase.
'''

def spell_1(*args):
    result = {}
    
    if args:
        for word in args:
            first_letter = word.lower()[0]
            current_word_length = len(word) 

            if first_letter not in result:
                result[first_letter] = current_word_length
            else:
                previous_word_length = result[first_letter]
                
                if previous_word_length < current_word_length:
                    result[first_letter] = current_word_length
    
    return result

def spell_2(*args):
    result = {}
    for word in args:
        if result.get(word[0].lower(), 0) < len(word):
            result[word[0].lower()] = len(word)
    return result