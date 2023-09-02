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


def init_line(start_x, end_x, start_y, end_y, width, colour):

    new_line = gr.Line(gr.Point(start_x, start_y), gr.Point(end_x, end_y))

    new_line.setWidth(width)

    new_line.setOutline(colour)

    return new_line


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
    eyebrow = init_line(start_x, end_x, point_y, point_y, width, colour)

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


def get_mouth(head_x, head_y, head_rad, colour, width):

    start_mouth_x = head_x - head_rad / 3
    end_mouth_x = head_x + head_rad / 3
    
    mouth_y = head_y + head_rad / 2 

    mouth = init_line(start_mouth_x, end_mouth_x, mouth_y, mouth_y, 2.5, "black")

    return mouth


def get_carrot(head_x, head_y, head_rad, width, colour):
    offset_x = (head_rad / 3)
    offset_y = (head_rad / 5) * 1.5

    carrot_start_x = head_x
    carrot_end_x = head_x - offset_x

    carrot_start_y = head_y
    carrot_end_y = head_y + offset_y

    carrot = init_line(carrot_start_x, carrot_end_x, carrot_start_y, carrot_end_y, width, colour)
    
    return carrot


def get_face(head_x, head_y, head_r):
    face = []

    eyes =  get_eyes(head_x, head_y, head_r, "black")
    mouth = get_mouth(head_x, head_y, head_r, 2.5, "black")
    carrot = get_carrot(head_x, head_y, head_r, 5, "orange")

    face.append(eyes)
    face.append(mouth)
    face.append(carrot)

    return face   


def draw_face(face, window):
    face[0][0].draw(window)
    face[0][1].draw(window)
    face[0][2].draw(window)
    face[0][3].draw(window)

    face[1].draw(window)

    face[2].draw(window)


def draw_head_return_sets(body_x, body_y, body_r, body_cl, window):
    head_ball, head_ball_sets = get_next_ball(body_x, 
                                              body_y, 
                                              body_r, 
                                              body_cl)
    head_ball.draw(window)
    
    face = get_face(head_ball_sets[0], 
                    head_ball_sets[1], 
                    head_ball_sets[2])
    draw_face(face, window)

    return head_ball_sets


def get_fingers(hand_end_x, hand_end_y, body_r, hand_side_flag):
    fingers = []

    offset = (body_r / 10) * hand_side_flag


    finger_1 = init_line(hand_end_x, 
                         hand_end_x + offset, 
                         hand_end_y,
                         hand_end_y,
                         2, "black")
    
    finger_2 = init_line(hand_end_x, 
                         hand_end_x + offset, 
                         hand_end_y,
                         hand_end_y + offset,
                         2, "black")
    
    finger_3 = init_line(hand_end_x, 
                         hand_end_x, 
                         hand_end_y,
                         hand_end_y + offset,
                         2, "black")

    fingers.append(finger_1)
    fingers.append(finger_2)
    fingers.append(finger_3)

    return fingers


def get_hand(body_x, body_y, body_r, hand_side):

    hand_side_flag = 0

    if hand_side == "left":
        hand_side_flag = -1
    elif hand_side == "right":
        hand_side_flag = 1
        
    hand_start_x = body_x + (body_r * hand_side_flag)
    hand_end_x = hand_start_x + (body_r * hand_side_flag)

    hand_start_y = body_y
    hand_end_y = hand_start_y + (body_r / 2)

    hand = init_line(hand_start_x, 
                    hand_end_x, 
                    hand_start_y, 
                    hand_end_y, 
                    2.5, "black")
    
    fingers = get_fingers(hand_end_x, hand_end_y, body_r, hand_side_flag)
    
    return hand, fingers


def draw_hands(body_x, body_y, bode_r, window):
    r_hand, r_fingers = get_hand(body_x, body_y, bode_r, "right")
    l_hand, l_fingers = get_hand(body_x, body_y, bode_r, "left")

    r_hand.draw(window)
    r_fingers[0].draw(window)
    r_fingers[1].draw(window)
    r_fingers[2].draw(window)

    l_hand.draw(window)
    l_fingers[0].draw(window)
    l_fingers[1].draw(window)
    l_fingers[2].draw(window) 


def draw_body_return_sets(bottom_x, bottom_y, bottom_r, body_cl ,window):
    middle_ball, middle_ball_sets = get_next_ball(bottom_x, 
                                              bottom_y, 
                                              bottom_r, 
                                              body_cl)
    
    middle_ball.draw(window)

    draw_hands(middle_ball_sets[0],
               middle_ball_sets[1],
               middle_ball_sets[2],
               window)

    return middle_ball_sets


def draw_bottom_return_sets(x, y, radius, color, window):
    bottom_ball, bottom_ball_sets = get_next_ball(x, y, radius, color)
    bottom_ball.draw(window)

    return bottom_ball_sets


def draw_snowman(x_size, y_size):
    window = gr.GraphWin("Draw a snowman project", x_size, y_size)

    body_colour = "#d9d9d9"

    start_rad = 125
    start_x = x_size / 2
    start_y = y_size - start_rad

    bottom_ball_sets = draw_bottom_return_sets(start_x, 
                                               start_y, 
                                               start_rad, 
                                               body_colour, 
                                               window)

    middle_ball_sets = draw_body_return_sets(bottom_ball_sets[0], 
                                             bottom_ball_sets[1], 
                                             bottom_ball_sets[2],
                                             body_colour, 
                                             window)

    head_ball_sets = draw_head_return_sets(middle_ball_sets[0], 
                                           middle_ball_sets[1], 
                                           middle_ball_sets[2],
                                           body_colour, 
                                           window)
    
    return window

def main():
    x_size = 1000
    y_size = 800

    window = draw_snowman(x_size, y_size)

    window.getMouse()

    window.close()


main()