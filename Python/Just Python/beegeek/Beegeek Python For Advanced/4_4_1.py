'''
TODO: Two natural numbers n and m are given as input to the program.
Write a program to create a matrix of size n×m, filling it with symbols. and * in a checkerboard pattern.
There should be a dot in the upper left corner.
Display the resulting matrix on the screen, separating elements with spaces.
'''


def get_even_row(columns):
    row = []
    
    for j in range(columns):
        if 0 == j % 2:
            row.append(".")
        else:
            row.append("*")
    
    return row


def get_odd_row(columns):
    row = []
    
    for j in range(columns):
        if 0 == j % 2:
            row.append("*")
        else:
            row.append(".")
    
    return row


def get_matrix(rows, columns):
    matrix = []

    for i in range(rows):
        if 0 == i % 2:
            matrix_row = get_even_row(columns)
        else:
            matrix_row = get_odd_row(columns)
            
        matrix.append(matrix_row)
    
    return matrix


def get_matrix_size():
    matrix_size = input().split()
    
    rows = int(matrix_size[0])
    columns = int(matrix_size[1])
    
    return(rows, columns)

def print_matrix_rows(matrix):
    for row in matrix:
        print(*row)
    

n, m = get_matrix_size()
matrix = get_matrix(n, m)

print_matrix_rows(matrix)