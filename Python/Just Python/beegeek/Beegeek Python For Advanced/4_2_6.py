'''
TODO: Write a program that prints the maximum element in the shaded region of a square matrix (2.png).

NOTE:Elements of the main diagonal are also taken into account.
'''

n = int(input())
matrix = []

for _ in range(n):
    row = [int(i) for i in input().split()]
    matrix.append(row)
    
largest = matrix[0][0]

for i in range(n):
    for j in range(n):
        if (i >= j and i + j + 1 <= n) or (i <= j and i + j + 1 >= n):
            if matrix[i][j] > largest:
                largest = matrix[i][j]
                
print(largest)