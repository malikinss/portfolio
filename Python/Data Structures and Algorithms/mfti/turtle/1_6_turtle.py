# Draw a spider with n legs.


import turtle


turtle.shape('turtle')


def draw_leg(leg_length):
    turtle.forward(leg_length)
    turtle.stamp()
    turtle.backward(leg_length)
    

def draw_spider(legs_length, legs_number):
    for i in range(legs_number):
        draw_leg(legs_length)

        turtle.left(360 / legs_number)


draw_spider(100, 12)