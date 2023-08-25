# Draw two stars, one with 5 vertices and the other with 11. 
# Use the function that draws a star with n vertices.


import turtle


def init_turtle(drawing_speed: int):
    turtle.shape('turtle')
    turtle.speed(drawing_speed)


def goto_without_lines(x_point, y_point):
    turtle.penup()
    turtle.goto(x_point, y_point)
    turtle.pendown()


def make_indent(indent): 
    turtle.penup()
    turtle.forward(indent)
    turtle.pendown()


def draw_david_star(size):
    size = size / 3
    for _ in range(6):
        turtle.forward(size)
        turtle.right(120)
        turtle.forward(size)
        turtle.left(60)


def draw_octagram(size, n):
    size = size / 3

    angle = (360 / n) + (360 / (n // 2))
    for _ in range(n):
        turtle.forward(size)
        turtle.left(angle)


def number_vertices_even(number_vertices, size):
    if number_vertices == 6:
        draw_david_star(size)
    else:
        draw_octagram(size)

    
def number_vertices_odd(number_vertices, size):
    angle_between_vertices = 180 - (180 / number_vertices)
    
    for _ in range (number_vertices):
        turtle.left(angle_between_vertices)
        turtle.forward(size)


def init_n_vertices_star(size, number_vertices):
    if 5 > number_vertices:
        print('Incorrect input')
    elif number_vertices % 2 == 0:
        number_vertices_even(number_vertices, size) # doesnt work for divided by 6
    else:
        number_vertices_odd(number_vertices, size)
    

def draw_n_vertices_star(speed, size, vertices):
    init_turtle(speed)
    init_n_vertices_star(size, vertices)

    turtle.hideturtle()
    turtle.exitonclick()


def main():
    draw_n_vertices_star(1, 200, 5)


if __name__ == "__main__":
    main()