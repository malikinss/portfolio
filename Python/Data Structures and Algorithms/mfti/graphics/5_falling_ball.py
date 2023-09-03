import graphics as gr


def add(point_1, point_2):
    new_point = gr.Point(point_1.x + point_2.x,
                         point_1.y + point_2.y)

    return new_point


def draw_ball(coords):
    circle = gr.Circle(coords, 10)
    circle.setFill('red')

    circle.draw(window)


def clear_window():
    rectangle = gr.Rectangle(gr.Point(0, 0), gr.Point(SIZE_X, SIZE_Y))
    rectangle.setFill('white')
    rectangle.draw(window)


def check_coords(coords, velocity):
    if coords.x < 0 or coords.x > SIZE_X:
        velocity.x = -velocity.x

    if coords.y < 0 or coords.y > SIZE_Y:
        velocity.y = -velocity.y


def update_velocity(velocity, acceleration):
    return add(velocity, acceleration)


def update_coords(coords, velocity):
    return add(coords, velocity)


SIZE_X = 400
SIZE_Y = 400

window = gr.GraphWin("Model", SIZE_X, SIZE_Y)

#  Начальное положение шарика
coords = gr.Point(SIZE_X / 2, SIZE_Y/ 2)
#  Скорость
velocity = gr.Point(1, -2)

acceleration = gr.Point(0, 0.1)

while True:
    clear_window()
    draw_ball(coords)

    coords = update_coords(coords, velocity)
    velocity = update_velocity(velocity, acceleration)
    check_coords(coords, velocity)

    gr.time.sleep(0.02)


