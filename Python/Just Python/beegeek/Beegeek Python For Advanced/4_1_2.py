'''
TODO: The number n is given as input to the program.
Write a program that creates and displays a line-by-line nested list of n lists [[1], [1, 2], [1, 2, 3], ..., [1, 2, ..., n]] .
'''

n = int(input())
result = []

for i in range(1, n + 1):
    result.append(list(range(1, i + 1)))

print(*result, sep='\n')
    