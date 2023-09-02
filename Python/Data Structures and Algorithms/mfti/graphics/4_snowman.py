import graphics as gr


def get_a_circle(point_x, point_y, radius, colour):
    '''This function creates a new coloured circle'''
    new_circle = gr.Circle(gr.Point(point_x, point_y), radius)
    new_circle.setFill(colour)
    
    return new_circle


def get_y_for_new_ball(previous_y, previous_diameter, current_diameter, percentage):
    '''
    This function calculates and returns new y coordinate 
    for new ball (not include bottom ball) 
    '''
    new_y = (previous_y - (previous_diameter + current_diameter)) * percentage
    return new_y


def get_new_ball_sets(prev_x, prev_y, prev_rad, size_percent, indent_percent):
    '''
    This function calculates and returns new coordinates 
    and radius of new ball (not include bottom ball)
    '''
    current_ball = []

    cur_rad = prev_rad * size_percent
    cur_x = prev_x

    cur_y = get_y_for_new_ball(prev_y, prev_rad, cur_rad, indent_percent)

    current_ball.append(cur_x)
    current_ball.append(cur_y)
    current_ball.append(cur_rad)

    return current_ball


def get_next_ball(prev_x, prev_y, prev_rad, colour):
    '''
    This function gets and returns the coordinates 
    for next ball and next ball object
    '''
    next_ball_sets = get_new_ball_sets(prev_x, 
                                       prev_y, 
                                       prev_rad, 
                                       size_percent=0.8, 
                                       indent_percent=1.1)
    
    next_ball = get_a_circle(next_ball_sets[0], 
                            next_ball_sets[1], 
                            next_ball_sets[2], 
                            colour)
    
    return next_ball, next_ball_sets


def get_eye_x(head_x, head_rad, eye_side):
    '''This function calculates and returns new x coordinate for eye'''
    eye_x = 0
    side_flag = 0

    if eye_side == "right":
        side_flag = 1
    elif eye_side == "left":
        side_flag = -1

    eye_x = head_x + (((head_rad / 3) * 1.75) * side_flag)
    return eye_x


def init_eyebrow(start_x, end_x, point_y, width, colour):

    eyebrow = gr.Line(gr.Point(start_x, point_y), gr.Point(end_x, point_y))

    eyebrow.setWidth(width)

    eyebrow.setOutline(colour)

    return eyebrow


def get_eyebrows_y(eye_y, eyebrow_width, eye_rad):
    '''This function calculates and returns new y coordinate for eyebrows'''
    
    eyebrow_y = eye_y - (((eyebrow_width / 2) + (eye_rad / 2)) * 2)
    return eyebrow_y


def get_eyebrow_x_coords(eye_x, eye_rad):
    half_of_len = eye_rad * 1.5
    start_x = eye_x - half_of_len
    end_x = eye_x + half_of_len

    return start_x, end_x 


def get_eyebrow(eye_x, eye_y, eye_rad):
    eyebrow_width = 5
    eyebrow_colour = "black"

    eyebrow_y = get_eyebrows_y(eye_y, eyebrow_width, eye_rad)
    
    eyebrow_coords_x = get_eyebrow_x_coords(eye_x, eye_rad)

    eyebrow = init_eyebrow(eyebrow_coords_x[0], 
                          eyebrow_coords_x[1], 
                          eyebrow_y, 
                          eyebrow_width, 
                          eyebrow_colour)

    return eyebrow

def get_eyes(head_x, head_y, head_rad, eye_colour):
    new_eyes = []

    eye_rad = head_rad * 0.2

    left_eye_x = get_eye_x(head_x, head_rad, "left")
    right_eye_x = get_eye_x(head_x, head_rad, "right") 

    eye_y = head_y

    left_eye = get_a_circle(left_eye_x, eye_y, eye_rad, eye_colour)
    right_eye = get_a_circle(right_eye_x, eye_y, eye_rad, eye_colour)

    new_eyes.append(left_eye)
    new_eyes.append(right_eye)

    left_eyebrow = get_eyebrow(left_eye_x, eye_y, eye_rad)
    right_eyebrow = get_eyebrow(right_eye_x, eye_y, eye_rad)
    
    new_eyes.append(left_eyebrow)
    new_eyes.append(right_eyebrow)

    return new_eyes





def draw_head(head_ball, l_eye, r_eye, l_eyebrow, r_eyebrow, window):
    head_ball.draw(window)
    l_eye.draw(window)
    r_eye.draw(window)
    l_eyebrow.draw(window)
    r_eyebrow.draw(window)


def draw_body(bottom_ball, middle_ball, window):
    bottom_ball.draw(window)
    middle_ball.draw(window)



def draw_snowman(head_ball,
                 middle_ball,  
                 bottom_ball, 
                 l_eye, 
                 r_eye, 
                 l_eyebrow, 
                 r_eyebrow,
                 window):
    
    head_ball.draw(window)
    l_eye.draw(window)
    r_eye.draw(window)
    l_eyebrow.draw(window)
    r_eyebrow.draw(window)

    middle_ball.draw(window)
    
    bottom_ball.draw(window)


x_size = 1000
y_size = 800

window = gr.GraphWin("Draw a snowman project", x_size, y_size)

body_colour = "#d9d9d9"

start_rad = 125
start_x = x_size / 2
start_y = y_size - start_rad

bottom_ball, bottom_ball_sets = get_next_ball(start_x, 
                                              start_y, 
                                              start_rad, 
                                              body_colour)

middle_ball, middle_ball_sets = get_next_ball(bottom_ball_sets[0], 
                                              bottom_ball_sets[1], 
                                              bottom_ball_sets[2], 
                                              body_colour)

head_ball, head_ball_sets = get_next_ball(middle_ball_sets[0], 
                                          middle_ball_sets[1],
                                          middle_ball_sets[2], 
                                          body_colour)

eyes =  get_eyes(head_ball_sets[0], 
                 head_ball_sets[1], 
                 head_ball_sets[2],
                 "black")


draw_snowman(head_ball, middle_ball, bottom_ball, 
             eyes[0], eyes[1], eyes[2], eyes[3], window)


window.getMouse()

window.close()