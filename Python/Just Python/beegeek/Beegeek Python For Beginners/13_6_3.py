'''
TODO: WWrite a function solve(a, b, c) that takes as arguments three integers a, b, c – the coefficients of the quadratic equation ax^2+bx+c=0 and returns its roots in ascending order.
'''


def solve(a, b, c):
    D = b ** 2 - 4 * a * c
    
    x1 = (-b - D ** 0.5) / (2 * a)
    x2 = (-b + D ** 0.5) / (2 * a)
    
    return min(x1, x2), max(x1, x2)
        


a, b, c = int(input()), int(input()), int(input())

x1, x2 = solve(a, b, c)

print(x1, x2)