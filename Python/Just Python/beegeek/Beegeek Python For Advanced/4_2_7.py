'''
TODO: The square matrix is divided into four quarters, bounded by the main and secondary diagonals: upper, lower, left and right.

NOTE: Diagonal elements are not taken into account.
'''

n = int(input())
matrix = []
quadrants = [['Верхняя четверть:', 0], 
             ['Правая четверть:', 0],
             ['Нижняя четверть:', 0], 
             ['Левая четверть:', 0]]

for _ in range(n):
    row = [int(i) for i in input().split()]
    matrix.append(row)

for i in range(n):
    for j in range(n):
        if i < j and i + j + 1 < n :
            quadrants[0][1] += matrix[i][j]
        elif i < j and i + j + 1 > n:
            quadrants[1][1] += matrix[i][j]
        elif i > j and i + j + 1 > n:
            quadrants[2][1] += matrix[i][j]
        elif i > j and i + j + 1 < n:
            quadrants[3][1] += matrix[i][j]

for i in range(4):
    print(quadrants[i][0], quadrants[i][1])