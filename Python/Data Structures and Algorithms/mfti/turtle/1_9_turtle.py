# Draw 10 nested regular polygons.
  

import math
import turtle


def init_turtle(drawing_speed):
    turtle.shape('turtle')
    turtle.speed(drawing_speed)


def get_angle(number):
    angle = ((number - 2) / number) * 180
    return angle


def init_polygon(number, border_length):
    angle = get_angle(number)
    turtle.left(180 - angle / 2)

    for i in range(number):
        turtle.forward(border_length)
        turtle.left(180 - angle)

    turtle.right(180 - angle / 2)


def make_indent(indent): 
    # indent - Increasing the length of the radius
    turtle.penup()
    turtle.forward(indent)
    turtle.pendown()


def get_side_length(radius, num_of_sides):
    length = 2 * radius * math.sin(math.pi / num_of_sides)
    return length


def draw_regular_poligons(number, R, indent):
    for num_of_sides in range(3, number):
        side_length = get_side_length(R, num_of_sides)
        init_polygon(num_of_sides, side_length)
        make_indent(indent)
        R += indent

init_turtle(10)
draw_regular_poligons(13, 40 , 20)
