""" 
Task: The input to the program is a string of genetic code consisting 
of the letters A (adenine), G (guanine), C (cytosine), T (thymine). 

Write a program that counts how many adenine, guanine, cytosine and 
thymine are included in a given line of the genetic code.
"""

given_string = input()
given_string = given_string.lower()

adenine = given_string.count('a')
guanine = given_string.count('g')
cytosine = given_string.count('c')
thymine = given_string.count('t')

print('Adenine:', adenine)
print('Guanine:', guanine)
print('Cytosine:', cytosine)
print('Thymine:', thymine)