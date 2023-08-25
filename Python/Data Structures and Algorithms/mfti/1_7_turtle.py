# Draw a "circle" spiral.


import turtle

def init_turtle(drawing_speed):
    turtle.shape('turtle')
    turtle.speed(drawing_speed)


def init_vortex():
    for i in range(1, 360*5):
        turtle.forward(i*0.00125)
        turtle.left(1)


def draw_vortex(drawing_speed):    
    init_turtle(drawing_speed)
    init_vortex()


draw_vortex(1000)    
