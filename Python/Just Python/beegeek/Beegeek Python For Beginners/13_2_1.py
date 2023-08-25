'''
TODO: Write a draw_triangle(fill, base) function that takes two parameters:

-- fill is a fill character;
-- base - the value of the base of an isosceles triangle;

and then outputs it.

NOTE: It is guaranteed that the base of the triangle is an odd number.
'''


# function declaration
def draw_triangle(fill, base):
    for i in range(1, base + 1):
        print(fill * min(i, base - i + 1))


fill = input()
base = int(input())

draw_triangle(fill, base)