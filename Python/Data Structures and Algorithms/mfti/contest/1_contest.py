

def sum_of_numbers(given_number = int(input())):
    result = 0
    for _ in range(3):
        result += given_number % 10
        given_number //= 10
    return(result)     

1
to_print = sum_of_numbers()
print(to_print)