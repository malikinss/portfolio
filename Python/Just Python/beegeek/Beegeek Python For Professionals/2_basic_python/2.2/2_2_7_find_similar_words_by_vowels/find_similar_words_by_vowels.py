'''
TODO:   
        Write a program that finds all similar words for a given word. 

        Words are called similar if they have the same number and arrangement of vowel letters. 

        At the same time, the vowels themselves may differ. 

        The program is given one word written in the first line, then a natural number n — the number of words to compare and n lines with words.

        The program should output all similar words for a given word, preserving their original order.

NOTE:   
        After the last vowel, there can be any number of consonants in the initial and checked word.

        In Russian, there are 10 vowel letters (а, у, о, ы, и, э, я, ю, ё, е) and 21 consonant letters (б, в, г, д, ж, з, к, л, м, н, п, р, с, т, ф, х, ц, ч, ш).
'''

def create_vowel_consonant_pattern(word, vowels, consonants):
    """
    Creates a pattern representing the arrangement of vowels and consonants in a given word.

    :param word: The input word
    :param vowels: Set of vowel letters
    :param consonants: Set of consonant letters
    :return: A pattern string indicating the arrangement of vowels and consonants
    """
    pattern = ''
    
    for letter in word.lower():
        if letter in vowels:
            pattern += 'v'
        elif letter in consonants:
            pattern += 'c'

    return pattern

def get_list_of_words(quantity_of_words):
    """
    Gets a list of words from the user input.

    :param quantity_of_words: The number of words to be entered
    :return: List of entered words
    """
    words = []

    for _ in range(quantity_of_words):
        word = input()
        words.append(word)

    return words

def compare_word_to_pattern(given_pattern, given_word, vowels, consonants):
    """
    Compares a given word to a pattern, checking if they have the same number and arrangement of vowels and consonants.

    :param given_pattern: Pattern to compare against
    :param given_word: Word to be compared
    :param vowels: Set of vowel letters
    :param consonants: Set of consonant letters
    :return: True if the word matches the pattern, False otherwise
    """
    if len(given_pattern) > len(given_word):
        return False
    
    
    given_word_pattern = create_vowel_consonant_pattern(given_word, vowels, consonants)
    given_pattern_vowels_quantity = given_pattern.count('v')
    given_word_pattern_vowels_quantity = given_word_pattern.count('v')

    is_vowels_num_equal = (given_pattern_vowels_quantity == given_word_pattern_vowels_quantity)
    are_vowels_cons_correct_order = (given_pattern == given_word_pattern[:len(given_pattern)])

    return is_vowels_num_equal and are_vowels_cons_correct_order

def find_similar_words_by_vowels(word_to_compare, vowels, consonants):
    """
    Finds all similar words for a given word based on the number and arrangement of vowels and consonants.

    :param word_to_compare: The word to compare against
    :param vowels: Set of vowel letters
    :param consonants: Set of consonant letters
    :return: List of similar words
    """
    general_pattern = create_vowel_consonant_pattern(word_to_compare, vowels, consonants)
    general_pattern = general_pattern[:general_pattern.rfind('v')+1]
    given_words = get_list_of_words(int(input()))
    filtered_words = [word for word in given_words if compare_word_to_pattern(general_pattern, word, vowels, consonants)]

    return filtered_words

# Define sets of vowel and consonant letters in Russian
RU_VOWELS = set(['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е'])
RU_CONSONANTS = set(['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш'])

# Find and print similar words
result = find_similar_words_by_vowels(input(), RU_VOWELS, RU_CONSONANTS)
print(*result, sep='\n')