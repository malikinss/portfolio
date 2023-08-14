""" 
Task: The input to the program is one string with the letters 
of the Russian language. Write a program that determines the 
number of vowels and consonants.
"""

given_string = input()

vowels = 'aeiouAEIOU'
consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'

vowels_cnt = 0
consonants_cnt = 0

for i in range(0,len(given_string)):
    if given_string[i] in vowels:
        vowels_cnt += 1
    
    if given_string[i] in consonants:
        consonants_cnt += 1

print('The number of vowels is', vowels_cnt)
print('The number of consonants is', consonants_cnt)