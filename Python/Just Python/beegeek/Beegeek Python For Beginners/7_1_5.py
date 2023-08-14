""" 
Task: Write a program that reads one line of text and outputs 10 lines, 
numbered 0 to 9, each with a specified line of text.
"""

given_sentence = input()

for i in range(10):
    print(i, given_sentence)