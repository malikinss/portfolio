for i in range(1, 100):
    flag = False
    number = i

    while number > 0:
        cur_digit = number % 10

        if cur_digit == 2:
            flag = True

        number = number // 10    

    if flag:
        continue

    print(i)        