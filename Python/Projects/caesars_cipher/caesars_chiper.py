'''
Project Description:

This Python program is designed to encrypt or decrypt a line of text in English, where each word in the input string is individually encrypted or decrypted using a Caesar cipher with a cyclic shift based on the length of the respective word. 
The Caesar cipher preserves the case of the letters, ensuring that lowercase letters remain lowercase, and uppercase letters remain uppercase. 
Additionally, the program assumes that there is a single space character between different words in the input string.

This project aims to provide a versatile tool for encrypting and decrypting text using a customizable Caesar cipher based on word lengths.

Usage:
    The program takes an input string of text, performs the specified encryption or decryption operation on each word within the text, and returns the modified text while maintaining the original word boundaries.

Example Usage:
    - Encrypting: "Hello World" -> "Lipps Asvph"
    - Decrypting: "Lipps Asvph" -> "Hello World"

'''


from random import randint
import os
import time


def clear_screen(seconds):
    time.sleep(seconds)
    os.system('cls')


def hello_user(name):
    print('\n Hello ', name)
    clear_screen(2)


def outro(name):
    print("\n Goodbye", name)
    clear_screen(2)  


def post_intro():
    print("\n Now I'm going to ask you to answer a few questions.\n Well let's get started.\n")
    clear_screen(3.5)


def intro():
    clear_screen(1)
    print("\n Hello my name is Caesar and I will help you encrypt or decrypt a message using my cipher.")
    print(' What is your name?\n')


def input_err():
    print('\n Incorrect input, please try again!')
    clear_screen(1)


def get_user_input():
    answer = input('\n Please enter your answer and press enter...\n')
    clear_screen(1)

    return answer


def is_input_empty(user_input):
    '''
    Checks if the user has submitted an empty value.

    Parameters:
        user_input (str): The user's input.

    Returns:
        bool: True if the input is empty, False otherwise.
        str: Corresponding message to be displayed on the screen.
    '''
    if user_input == '':
        print("\n You didn't enter anything")
        clear_screen(1)

        return True
    
    return False


def get_correct_user_input():
    '''
    Takes input from the user and checks if it's empty. 
    If it's empty, it asks for input again.
    If not, it returns the data received from the user.

    Returns:
        user_input (str): non-empty input provided by the user.
    '''
    flag = True

    while flag:
        user_input = get_user_input()
        flag = is_input_empty(user_input)

    return user_input  


def print_main_menu():
    clear_screen(0.5)
    print("\n What do you want to do? \n Enter the number of one of the options below.")
    print(" 1. I want to encrypt a message")
    print(" 2. I want to decrypt the message")


def get_len_of_each_word_list(list_of_words):
    len_of_words = []

    for word in list_of_words:
        len_of_words.append(len(word))

    return len_of_words


def get_new_ascii_position(letter, shift, mode):
    if mode == 'encrypt':
        new_ascii_position = ord(letter) + shift
                    
        if new_ascii_position > 90 and new_ascii_position < 97:
            new_ascii_position = (new_ascii_position - 90) + 64
        
        elif new_ascii_position > 122:
            new_ascii_position = (new_ascii_position - 122) + 96

    elif mode == 'decrypt':
        new_ascii_position = ord(letter) - shift
                    
        if new_ascii_position > 90 and new_ascii_position < 97:
            new_ascii_position = new_ascii_position + 26
        
        elif new_ascii_position < 65:
            new_ascii_position = new_ascii_position + 26

    return new_ascii_position    


def get_encrypted_or_decrypted_str(what_to_do, words):
    new_string = ''

    for word in words:
        len_of_word = len(word)
        new_word = ''

        if word.isalpha():
            for letter in word:
                new_ascii_position = get_new_ascii_position(letter, len_of_word, what_to_do)

                new_letter = chr(new_ascii_position)

                new_word += new_letter
        else:
            new_word = word

        new_string += new_word
        new_string += ' '

    return new_string    


def get_words_list_from_user_input():
    string_from_user = get_correct_user_input()
    list_of_words_from_string = string_from_user.split()
    
    return list_of_words_from_string

def encrypt_caesar_cipher():
    print("\n Please enter the text you want to encrypt. \n Words in a line must be separated by one space!")
    
    words_to_encrypt = get_words_list_from_user_input()

    new_string = get_encrypted_or_decrypted_str('encrypt', words_to_encrypt)

    return new_string


def decrypt_caesar_cipher():
    print("\n Please enter the text you want to decrypt. \n Words in a line must be separated by one space!")
    
    words_to_decrypt = get_words_list_from_user_input()

    new_string = get_encrypted_or_decrypted_str('decrypt', words_to_decrypt)

    return new_string


def save_to_the_result_file(string_to_save):
    current_directory = os.getcwd()

    file_name = "result.txt"

    file_path = os.path.join(current_directory, file_name)

    with open(file_path, 'w') as result_file:
        result_file.write(string_to_save + '\n')
        
        result_file.close()

    print('\nThe result is written to the file result.txt')


def select_and_execute_operating_mode():
    flag = False

    while flag == False:
        selected_operating_mode = get_correct_user_input()

        if selected_operating_mode == '1':
            result_string = encrypt_caesar_cipher()
            flag = True
        elif selected_operating_mode == '2':
            result_string = decrypt_caesar_cipher()
            flag = True
        else:
            input_err()
            flag = False  

    save_to_the_result_file(result_string)


def caesar_cipher():
    intro()

    username = get_correct_user_input()

    print_main_menu()
    select_and_execute_operating_mode()

    outro(username)


caesar_cipher()