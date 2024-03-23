'''
TODO:   Implement the hide_card() function, which takes one argument:

        card_number is a string representing the correct bank card number of 16 digits, between which there may be space characters

        The function should replace the first 12 digits in the card_number string with the * character and return the result. If there were space characters between the digits in the number, they should be deleted.
'''

def hide_card(card_number):
    corrected_card_number = ''

    for digit in card_number:
        if digit.isdigit():
            corrected_card_number += digit
        

    hided_card_number = '*' * 12 + corrected_card_number[-4:]

    return hided_card_number