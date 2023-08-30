def evens_in_sequence():
    x = 1
    counter = 0
    
    while x != 0:
        x = int(input())
        if x % 2 == 0 and x != 0:
            counter += 1

    print(counter)


evens_in_sequence()
