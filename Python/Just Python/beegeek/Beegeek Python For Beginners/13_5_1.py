'''
TODO: Write a function is_valid_triangle(side1, side2, side3) that takes three natural numbers as arguments, and returns True if there is a non-degenerate triangle with sides side1, side2, side3, and False otherwise.
'''


def is_valid_triangle(side1, side2, side3):

    expression_1 = side1 < side2 + side3
    expression_2 = side2 < side1 + side3
    expression_3 = side3 < side1 + side2

    if expression_1 and expression_2 and expression_3:
        return True
    else:
        return False


a, b, c = int(input()), int(input()), int(input())


print(is_valid_triangle(a, b, c))