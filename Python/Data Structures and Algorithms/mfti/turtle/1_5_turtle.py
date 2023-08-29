# Draw 10 nested squares.

import turtle


turtle.shape('turtle')


def make_indent(indent):
    turtle.penup()
    turtle.forward(indent)
    turtle.right(90)
    turtle.forward(indent)
    turtle.right(180)
    turtle.pendown()


def draw_square(border_length):
    for i in range(4):
        turtle.forward(border_length)
        
        if i != 3:
            turtle.left(90)


def draw_nested_squares(number, indent, start_border_size):
    for i in range(number):
        current_size = start_border_size + indent * i * 2

        draw_square(current_size)
        make_indent(indent)


draw_nested_squares(10, 10, 50)