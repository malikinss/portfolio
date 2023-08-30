def print_squares_to_n(n):
    square_of_i = 0

    for i in range(1, n):
        square_of_i = i ** 2
        
        if square_of_i <= n:
            print(square_of_i)
        else:
            break    

print_squares_to_n(int(input()))