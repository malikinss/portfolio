'''
TODO: The program receives two natural numbers n and m as input, each on a separate line - the number of rows and columns in the matrix. Next, the matrix elements themselves are introduced - words, each on a separate line; The elements of the first line are in a row, then the second, etc.

Write a program that reads the elements of a matrix one by one, outputs them as a matrix, outputs an empty row, and again the same matrix, but with the rows and columns swapped: the first row is output as the first column, and so on.
'''

n, m = int(input()), int(input())
matrix = []

for _ in range(n):
    row = [input() for j in range(m)]
    matrix.append(row)
    
for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=' ')

    print()

print()

for j in range(m):
    for i in range(n):
        print(matrix[i][j], end=' ')
        
    print()