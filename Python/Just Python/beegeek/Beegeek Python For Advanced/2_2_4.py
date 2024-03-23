'''
TODO: The input to the program is a text string of natural numbers. 
A list of numbers is formed from the elements of the string. Write a program to cyclically shift the elements of a list to the right, with the last element becoming the first and the rest moving one position forward, towards increasing indices.
'''

seq = input().split()
new_seq = [seq[-1]] + seq[:-1]

print(*new_seq)