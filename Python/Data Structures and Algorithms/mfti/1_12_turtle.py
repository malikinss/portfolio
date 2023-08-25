# Draw a "spring" using circles. 
  

import turtle


def init_turtle(drawing_speed: int):
    turtle.shape('turtle')
    turtle.speed(drawing_speed)


def get_turn(new_radius):
    turtle.circle(radius=-new_radius, extent=180)


def init_spring(num_of_turns, size):
    for i in range(num_of_turns):
        turtle.circle(radius=-size, extent=180)
        
        if i == (num_of_turns - 1): 
            #do not draw last internal turn
            break

        internal_turn_size = (size/(size // 10))
        turtle.circle(radius=-internal_turn_size, extent=180)


def draw_spring(speed, num_of_turns, size):
    turtle.left(90)
    init_turtle(speed)
    init_spring(num_of_turns, size)


draw_spring(5, 6, 50)