'''
TODO: Two natural numbers n and m are given as input to the program.
Write a program that creates an n×m matrix, filling it with "diagonals" according to the pattern.

n = 3 
m = 5

1  2  4  7  10
3  5  8  11 13
6  9  12 14 15
'''

def get_matrix_size():
    matrix_size = input().split()
    
    rows = int(matrix_size[0])
    columns = int(matrix_size[1])
    
    return(rows, columns)


def print_matrix(matrix):
    for row in matrix:
        print(*row)         
        

def get_empty_matrix(number_of_rows, number_of_columns):
    matrix = []
    
    for _ in range(number_of_rows):
        row = []
        for _ in range(number_of_columns):
            row.append(0)
        matrix.append(row)
        
    return matrix




def update_position(current_position, row, column, last_added_element):
    current_position['row'] = row
    current_position['column'] = column
    current_position['last_added_element'] = last_added_element
    
    return current_position


def get_position_data(current_position):
    row = current_position['row']
    column = current_position['column']
    last_added_element = current_position['last_added_element']
    
    return row, column, last_added_element




def fill_from_left_to_right(matrix, number_elements_in_row, current_position):
    element = 0 
    row, column, last_added_element = get_position_data(current_position)
    end_element_to_fill = number_elements_in_row + last_added_element
    
    for element in range(last_added_element + 1, end_element_to_fill + 1):
        matrix[row][column] = element
        column += 1
    
    last_added_element = element
    row += 1
    column -= 1
    
    current_position = update_position(current_position, row, column, last_added_element)
    
    return matrix, current_position


def fill_from_right_to_left(matrix, number_elements_in_row, current_position):
    element = 0 
    row, column, last_added_element = get_position_data(current_position)
    end_element_to_fill = number_elements_in_row + last_added_element
    
    for element in range(last_added_element + 1, end_element_to_fill + 1):
        matrix[row][column] = element
        column -= 1
    
    last_added_element = element
    row -= 1
    column += 1
    
    current_position = update_position(current_position, row, column, last_added_element)
    
    return matrix, current_position  


def fill_from_up_to_down(matrix, number_elements_in_column, current_position):
    element = 0 
    row, column, last_added_element = get_position_data(current_position)
    end_element_to_fill = number_elements_in_column + last_added_element
    
    for element in range(last_added_element + 1, end_element_to_fill + 1):
        matrix[row][column] = element
        row += 1
    
    last_added_element = element
    row -= 1
    column -= 1
    
    current_position = update_position(current_position, row, column, last_added_element)
    
    return matrix, current_position


def fill_from_down_to_up(matrix, number_elements_in_column, current_position):
    element = 0
    row, column, last_added_element = get_position_data(current_position)
    end_element_to_fill = number_elements_in_column + last_added_element
    
    for element in range(last_added_element + 1, end_element_to_fill + 1):
        matrix[row][column] = element
        row -= 1
    
    last_added_element = element
    row += 1
    column += 1
    
    current_position = update_position(current_position, row, column, last_added_element)
    
    return matrix, current_position 
    




def if_matrix_filled_change_flag(flag, current_position, rows, columns):
    final_element = rows * columns
    
    if current_position['last_added_element'] == final_element:
            flag = False
    
    return flag
    
def get_matrix(number_of_rows, number_of_columns):
    matrix = get_empty_matrix(number_of_rows, number_of_columns)
    
    current_position = dict(row = 0, column = 0, last_added_element = 0)
    
    number_elements_in_row = number_of_columns
    number_elements_in_column = number_of_rows
    
    flag = True
    
    while flag:
        
        matrix, current_position = fill_from_left_to_right(matrix, number_elements_in_row, current_position)
        number_elements_in_column -= 1
        print(current_position['last_added_element'], current_position['row'], current_position['column'])  
        print()
        
        flag = if_matrix_filled_change_flag(flag, current_position, number_of_rows, number_of_columns)
        
        matrix, current_position = fill_from_up_to_down(matrix, number_elements_in_column, current_position)
        number_elements_in_row -= 1
        print(current_position['last_added_element'], current_position['row'], current_position['column'])  
        print()
        
        flag = if_matrix_filled_change_flag(flag, current_position, number_of_rows, number_of_columns)
            
        matrix, current_position = fill_from_right_to_left(matrix, number_elements_in_row, current_position)
        number_elements_in_column -= 1
        print(current_position['last_added_element'], current_position['row'], current_position['column'])  
        print()
        
        flag = if_matrix_filled_change_flag(flag, current_position, number_of_rows, number_of_columns)
            
        matrix, current_position = fill_from_down_to_up(matrix, number_elements_in_column, current_position)
        number_elements_in_row -= 1
        print(current_position['last_added_element'], current_position['row'], current_position['column'])  
        print()
        
        flag = if_matrix_filled_change_flag(flag, current_position, number_of_rows, number_of_columns)
            
    return matrix
        
n, m = get_matrix_size()
matrix = get_matrix(n, m)
print_matrix(matrix)