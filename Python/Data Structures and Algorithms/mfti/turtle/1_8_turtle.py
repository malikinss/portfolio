# Draw a "square" spiral.


import turtle

def init_turtle(drawing_speed):
    turtle.shape('turtle')
    turtle.speed(drawing_speed)


def init_square_spiral(start_line_length, indent):
    for i in range(100):
        turtle.forward(start_line_length + indent * i)
        turtle.left(90)


def draw_square_spiral(drawing_speed, start_line_len, indent):
    init_turtle(drawing_speed)
    init_square_spiral(start_line_len, indent)


draw_square_spiral(5, 10, 5)