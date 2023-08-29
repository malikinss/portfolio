# Draw a "flower" using circles. 
  

import turtle


def init_turtle(drawing_speed: int):
    turtle.shape('turtle')
    turtle.speed(drawing_speed)


def draw_two_circles(size):
    turtle.circle(size)
    turtle.circle(-size)

# it works only with an even number of petals
def init_flower(size, petals): 
    for i in range(int(petals / 2)):
        turtle.left(360 / petals)
        draw_two_circles(size)
    

def draw_flower(speed, size, petals):
    init_turtle(speed)
    init_flower(size, petals)


draw_flower(10, 100, 6)