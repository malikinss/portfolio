# Draw a "butterfly" using circles. 
  

import turtle


def init_turtle(drawing_speed: int):
    turtle.shape('turtle')
    turtle.speed(drawing_speed)


def draw_two_circles(size):
    turtle.circle(size)
    turtle.circle(-size)


def init_butterfly(layers, start_size, increment_value):
    turtle.left(90)
    
    size = start_size
    
    for i in range(layers):
        draw_two_circles(size)
        size += increment_value 

def draw_butterfly(speed, layers, start_size, increment_value):
    init_turtle(speed)
    init_butterfly(layers, start_size, increment_value)


draw_butterfly(5, 10, 25, 5) 