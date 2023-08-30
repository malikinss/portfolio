def max_in_sequence():
    x = 1
    max = 0
    
    while x != 0:
        x = int(input())
        
        if x >= max:
            max = x

    print(max) 


max_in_sequence()
