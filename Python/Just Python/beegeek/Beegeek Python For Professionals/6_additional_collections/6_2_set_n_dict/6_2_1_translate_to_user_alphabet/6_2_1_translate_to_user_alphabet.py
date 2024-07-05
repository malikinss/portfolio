'''
TODO:
        Given a string of correspondence to the Latin alphabet: the first
        character of the string corresponds to the letter a, the second to b,
        the third to c, and so on.
        Each character corresponds to both uppercase and lowercase letters.
        The number of characters in the string matches the number of letters
        in the Latin alphabet.

        Write a program that uses this string to translate the given text.

        The first line of the program's input is a string of correspondence to
        the Latin alphabet, and the next line is the text to be translated.

        The program must use this string of correspondence to the
        Latin alphabet to translate the input text and output the result.

NOTE:
        The program must ignore all characters that are not Latin letters.
'''
from typing import Dict
from string import ascii_lowercase


def get_user_alphabet() -> Dict[str, str]:
    """
    Gets the user-provided alphabet correspondence and returns
    it as a dictionary.

    Returns:
        Dict[str, str]: A dictionary mapping each letter of the Latin alphabet
        to the corresponding character in the user-provided alphabet.
    """
    user_input = list(input())
    translation_map = dict(zip(ascii_lowercase, user_input))

    return translation_map


def translate_text(translation_map: Dict[str, str], text: str) -> str:
    """
    Translates the given text using the provided translation map.

    Args:
        translation_map (Dict[str, str]): A dictionary mapping each letter of
        the Latin alphabet to the corresponding character in the user-provided
        alphabet.
        text (str): The text to be translated.

    Returns:
        str: The translated text.
    """
    result_text = []

    for letter in text:
        lower_letter = letter.lower()
        translated_letter = translation_map.get(lower_letter, letter)
        result_text.append(translated_letter)

    return ''.join(result_text)


if __name__ == '__main__':
    user_alphabet = get_user_alphabet()
    string_to_translate = input()
    translated_text = translate_text(user_alphabet, string_to_translate)

    print(translated_text)
