'''
TODO: The program receives two natural numbers n and m as input, each on a separate line - the number of rows and columns in the matrix.

Next, the matrix elements themselves are introduced - words, each on a separate line; The elements of the first line are in a row, then the second, etc.

Write a program that first reads the elements of a matrix one by one, then outputs them as a matrix.
'''

n, m = int(input()), int(input())
matrix = []

for i in range(n):
    row = []

    for j in range(m):
        row.append(input())

    matrix.append(row)

for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=' ')
    
    print()