'''
TODO: Write a function is_correct_bracket(text) that takes as an argument a non-empty string text consisting of the characters ( and ) and returns True if the input string is a correct bracket sequence and False otherwise.

NOTE: A regular bracket sequence is a string consisting only of the characters ( and ), where each opening bracket has a matching closing bracket (and each opening bracket must be to the left of its corresponding closing bracket).
'''


def is_correct_bracket(text):
    while "()" in text:
        text = text.replace("()", "")
        
    return text == ""



txt = input()

print(is_correct_bracket(txt))