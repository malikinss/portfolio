# Draw a smile face :-). 
  

import turtle


def init_turtle(drawing_speed: int):
    turtle.shape('turtle')
    turtle.speed(drawing_speed)


def make_indent(indent): 
    turtle.penup()
    turtle.forward(indent)
    turtle.pendown()


def goto_without_lines(x_point, y_point):
    turtle.penup()
    turtle.goto(x_point, y_point)
    turtle.pendown()


def get_filled_circle(size, fill_color, border_color):
    turtle.color(border_color)
    turtle.fillcolor(fill_color)
    
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()


def get_eye(eye_size, color):
    get_filled_circle(eye_size, color, "black")


def get_eyes_pair(face_size):
    eye_size = (face_size / 9) * 2
    indent = face_size 

    get_eye(eye_size, "blue")
    make_indent(indent)
    get_eye(eye_size, "blue")


def goto_place_for_eyes(face_size):
    y_point = (face_size / 9) * 10
    x_point = -(face_size / 2)
    
    goto_without_lines(x_point, y_point)


def get_face(face_size):
    get_filled_circle(face_size, "yellow", "black")


def goto_place_for_nose(face_size):
    y_point = face_size
    x_point = 0
    
    goto_without_lines(x_point, y_point)
    
    turtle.right(90)


def get_nose(face_size):
    nose_size = face_size * 0.34
    nose_width = face_size / 9

    turtle.width(nose_width)
    turtle.forward(nose_size)
    turtle.width(1)


def goto_place_for_smile(face_size):
    y_point = face_size * 0.675
    x_point = face_size / 2
    
    goto_without_lines(x_point, y_point)


def get_smile(face_size):
    smile_size = -face_size * 0.5
    smile_width = face_size / 9

    turtle.color("red")
    turtle.width(smile_width)
    
    turtle.circle(radius=smile_size, extent=180)
    
    turtle.width(1)
    turtle.color("black")


def init_smileface(face_size):
    get_face(face_size)

    goto_place_for_eyes(face_size)
    get_eyes_pair(face_size)
    
    goto_place_for_nose(face_size)
    get_nose(face_size)

    goto_place_for_smile(face_size)
    get_smile(face_size)
    

def draw_smileface(speed, size):
    init_turtle(speed)
    init_smileface(size)


draw_smileface(7, 100)