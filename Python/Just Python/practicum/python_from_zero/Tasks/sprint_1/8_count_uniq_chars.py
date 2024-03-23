'''
TODO: 
        Find the number of unique characters in a string, excluding spaces.
'''

def count_uniq_chars(text):
    return len(set(text.replace(' ', '')))

not_uniq_str = 'eat some more of these soft French rolls and drink some tea'

print(count_uniq_chars(not_uniq_str))