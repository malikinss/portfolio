'''
TODO:
        Master Yoda grew old and became very poor in speech: he began to swap the first and last word of a phrase. 
        
        Write a program that can bring his phrases into normal form. 
        
        Without creating a new object, swap the first and last word.
'''

def correct_yoda_speech(text):
    first = text.pop(0)
    last = text.pop()

    text.insert(0, last)
    text.append(first)

    return text

force_words = ['you', 'the', 'force', 'be', 'with', 'may']
original_id = id(force_words)

force_words = correct_yoda_speech(force_words)
print(force_words)
print(id(force_words) == original_id)