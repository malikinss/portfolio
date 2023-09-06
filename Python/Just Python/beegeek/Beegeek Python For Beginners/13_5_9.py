'''
TODO: Write a function convert_to_python_case(text) that takes a camel case string as an argument and converts it to snake case.

NOTE: You can read more about naming styles here.
https://ru.wikipedia.org/wiki/CamelCase
'''


def convert_to_python_case(text):
    new_text = ""

    for el in text:
        # check that the element is in upper case (skip numbers)
        if not el == el.lower():  
            new_text += "_" + el.lower()
        else:
            new_text += el
            
    return new_text[1:]



txt = input()

print(convert_to_python_case(txt))