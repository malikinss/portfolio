'''
TODO: Write a function draw_triangle() that draws a star isosceles triangle with base and height equal to 15 and 8 respectively:
'''


def draw_triangle():
    m = 15

    for i in range(1, m + 1, 2):
        print(' ' * ((m - i) // 2) + '*' * i)


draw_triangle()