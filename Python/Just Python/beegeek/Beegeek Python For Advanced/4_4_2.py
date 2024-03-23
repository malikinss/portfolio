'''
TODO: The program input is a natural number n.
Write a program that creates an n×n matrix and fills it according to the following rule:
- the numbers on the side diagonal are equal to 1;
- numbers above this diagonal are equal to 0;
- the numbers below this diagonal are equal to 2.

Display the resulting matrix on the screen.
Separate numbers in a line with one space.
'''

def get_matrix_size():
    matrix_size = int(input())
    
    return matrix_size


def print_matrix_rows(matrix):
    for row in matrix:
        print(*row)


def get_row_with_side_diagonal(length, side_diagonal_index):
    row = []
    
    for current_column_index in range(length):
        if current_column_index < side_diagonal_index:
            row.append(0)
        
        elif current_column_index > side_diagonal_index:
            row.append(2)
        
        else:
            row.append(1)
            
    return row        


def get_matrix_with_side_diagonal(size):
    matrix = []

    for i in range(n):
        side_diagonal = n - 1 - i
    
        current_row = get_row_with_side_diagonal(n, side_diagonal)

        matrix.append(current_row)
        
    return matrix

    
n = get_matrix_size()
matrix = get_matrix_with_side_diagonal(n)
print_matrix_rows(matrix)