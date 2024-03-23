'''
TODO: Write a program that prints the number of elements of a square matrix in each row that are greater than the arithmetic mean of the elements of the given row.
'''

n = int(input())
matrix = []

for _ in range(n):
    row = [int(i) for i in input().split()]
    matrix.append(row)
    
for i in range(n):
    counter = 0
    average = sum(matrix[i]) / n
    for j in range(n):
        if matrix[i][j] > average:
            counter += 1
    print(counter)