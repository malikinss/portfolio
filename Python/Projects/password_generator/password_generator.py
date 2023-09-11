'''
DESCRIPTION: the program generates a predetermined number of passwords and includes smart settings for the length of the password, as well as which characters you want to include in it and which ones to exclude.
'''

from random import randint
import os
import time


DIGITS = '0123456789'
LOWERCASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
UPPERCASE_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
PUNCTUATION = '!#$%&*+-=?@^_'


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
    print('\n Hello, I am a Secure Password Generator and I will help you generate a strong password.')
    print(' What is your name?\n')


def input_err():
    print('\n Incorrect input, please try again!')
    clear_screen(1)


def get_user_input():
    answer = input('\n Please enter your answer and press enter...\n')
    clear_screen(1)

    return answer


def is_input_empty(user_input):
    if user_input == '':
        print("\n You didn't enter anything")
        clear_screen(1)

        return True
    
    return False


def get_correct_user_input():
    '''
    This function takes input from the user and checks if it's empty. If it's empty, it asks for input again. If not, returns the data received from the user.
    '''
    flag = True

    while flag:
        user_input = get_user_input()
        flag = is_input_empty(user_input)

    return user_input  


def check_num_of_passwords(user_answer):
    if user_answer.isdigit() and int(user_answer) > 0:
        return True
    
    input_err()

    return False


def get_number_of_passwords(question):
    input_coorect_flag = False

    while input_coorect_flag == False:
        print(question)
        user_answer = get_correct_user_input()
        input_coorect_flag == check_num_of_passwords(user_answer)
            
    return int(user_answer)



def check_len_of_password(user_answer):
    if user_answer.isdigit() and (int(user_answer) > 4 and int(user_answer) < 20):
        return True
    
    input_err()
    
    return False


def get_len_of_password(question):
    input_coorect_flag = False

    while input_coorect_flag == False:
        print(question)
        user_answer = get_correct_user_input()
        input_coorect_flag == check_len_of_password(user_answer)
            
    return int(user_answer)


def print_yes_or_no():
    print("\n if yes enter 'y'")
    print(" if no enter 'n': \n")


def get_yes_or_no(question):
    user_answer = ' '
    
    while user_answer != "Y" or user_answer != "N":
        print(question)
        print_yes_or_no()

        user_answer = get_correct_user_input()
        user_answer = user_answer.upper()

        if user_answer == 'N':
            return False

        elif user_answer == 'Y':
            return True
                
        else:
            input_err()

        clear_screen(2)    


def get_answers_for_questions():
    dict_keys_names = ['total',
                       'length',
                       'numbers',
                       'capitals',
                       'lowercase',
                       'symbols',
                       'ambigious_chars']

    questions = ["\n How many passwords do you want to generate",
                 "\n What should be the length of the password?\n Minimum is 4, Maximum is 20",
                 "\n Should the password include numbers?\n Example: 123",
                 "\n Should the password include capital letters?\n Example: XYZ",
                 "\n Should the password include lowercase letters?\n Example: abc",
                 "\n Should the password include special letter characters?\n Example: !#$%&*+-=?@^_",
                 "\n Should the password exclude ambiguous characters?\n Example: il1Lo0O"]
    
    answers = {}

    for i in range(len(questions)):
        if i == 0:
            number_of_passwords = get_number_of_passwords(questions[i])
            answers[dict_keys_names[i]] = number_of_passwords
        
        elif i == 1:
            password_length = get_len_of_password(questions[i])
            answers[dict_keys_names[i]] = password_length

        else:
            other_answers = get_yes_or_no(questions[i])
            answers[dict_keys_names[i]] = other_answers
    
    return answers

            
            




                


def password_generator():
    intro()
    name = get_correct_user_input()
    hello_user(name)
    post_intro()

    answers = get_answers_for_questions()
    print(answers)

    outro(name)


password_generator()


