'''
TODO:
        Write an implementation of closest_mod_5 that takes an integer x as its only argument and returns the smallest integer y such that:
            y is greater than or equal to x
            y is divisible by 5
'''

def closest_mod_5(x):
    if x % 5 == 0:
        return x
    
    while x % 5 != 0:
        x += 1
    return x

def closest_mod_5(x):
    remainder = x % 5

    if remainder > 0:
        return x + (5 - remainder)
    else:
        return x
