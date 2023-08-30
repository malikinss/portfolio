def log_2_from_number(number):
    k = 0
    
    while 2 ** k < number:
        k += 1
    
    print(k)


log_2_from_number(int(input()))