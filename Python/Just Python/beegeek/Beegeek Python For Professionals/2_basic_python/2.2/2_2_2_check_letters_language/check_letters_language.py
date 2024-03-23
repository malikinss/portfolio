'''
TODO:   
        There are letters in Russian and English that look the same.

        Here is a list of English letters “AaBCcEeHKMOoPpTXxy”, and here are their Russian analogues "АаВСсЕеНКМОоРрТХху".

        Write a program that, for three letters from given lists of letters, determines whether they are Russian, English, or both (a mixture of Russian and English letters).

        The program should output:
            - ru - if all three letters are Russian
            - en - if all three letters are English
            - mix - if the letters include both Russian and English

NOTE:   
        It is guaranteed that the three letters entered are in the set "AaBCcEeHKMOoPpTXxy" + "АаВСсЕеНКМОоРрТХху" (English + Russian letters).
'''
        
def check_letters_language(letters):
    """
    Determines the language of three letters (Russian, English, or both).

    :param letters: Three letters from the set "AaBCcEeHKMOoPpTXxy" + "АаВСсЕеНКМОоРрТХху"
    :return: 'ru' if all three letters are Russian, 'en' if all three letters are English, 'mix' if a mixture of Russian and English letters
    """
    russian_letters = 'АаВСсЕеНКМОоРрТХху'
    english_letters = 'AaBCcEeHKMOoPpTXxy'

    is_russian = any(letter in russian_letters for letter in letters)
    is_english = any(letter in english_letters for letter in letters)

    if is_russian and is_english:
        language = 'mix'
    elif is_russian:
        language = 'ru'
    elif is_english:
        language = 'en'
    else:
        language = 'unknown'  # A case for handling unexpected situations

    return language

# Test cases
print(check_letters_language('ABC'))  # Should print 'en'
print(check_letters_language('МНО'))  # Should print 'ru'
print(check_letters_language('ABCМ'))  # Should print 'mix'
