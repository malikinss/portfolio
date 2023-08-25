'''
The input to the program is a text string containing integers. Write a program using a list expression that will print the cubes of the specified numbers also on the same line.
'''

s = input()

lst = [int(i) ** 3 for i in s.split()]

print(*lst)