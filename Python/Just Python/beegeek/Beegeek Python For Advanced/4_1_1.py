'''
TODO: The number n is given as input to the program.
Write a program that creates and displays a list line by line consisting of n lists [[1, 2, ..., n], [1, 2, ..., n], ..., [1, 2, .. ., n]].
'''

n = int(input())
result = []

for _ in range(n):
    result.append(list(range(1, n + 1)))

print(*result, sep='\n')