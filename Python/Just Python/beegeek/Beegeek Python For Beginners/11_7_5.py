'''
The input to the program is a natural number n. 
Write a list expression program that generates a list containing the squares of numbers from 1 to n (inclusive), and then prints its elements line by line, that is, each on a separate line.
'''

print(*[i**2 for i in range(1,int(input())+1)], sep = '\n')