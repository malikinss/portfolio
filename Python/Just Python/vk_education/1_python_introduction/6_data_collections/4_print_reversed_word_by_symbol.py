def print_reversed_word_by_symbol(word):
    letter_count = -1

    while letter_count >= -len(word):
        print(word[letter_count])
        letter_count -= 1

print_reversed_word_by_symbol('word')