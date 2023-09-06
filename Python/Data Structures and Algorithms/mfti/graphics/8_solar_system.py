import graphics as gr


SIZE_X = 1200
SIZE_Y = 1200

CENTER_X = SIZE_X / 2
CENTER_Y = SIZE_Y / 2


def add(point_1, point_2):
    new_point = gr.Point(point_1.x + point_2.x,
                         point_1.y + point_2.y)

    return new_point


def sub(point_1, point_2):
    new_point = gr.Point(point_1.x - point_2.x,
                         point_1.y - point_2.y)

    return new_point


def get_circle(point_x, point_y, radius, colour):
    '''This function creates a new coloured circle'''
    new_circle = gr.Circle(gr.Point(point_x, point_y), radius)
    new_circle.setFill(colour)
    
    return new_circle


def get_planet(radius, prev_x, color):
    
    planet_x = prev_x + (10 * radius)
    planet_y = CENTER_Y
    
    planet = get_circle(planet_x, planet_y, radius, color)
    planet_border_x = planet_x + radius

    return planet, planet_border_x


def get_sun():
    
    sun_radius = SIZE_X / 100 * 5
    sun_x = CENTER_X
    sun_y = CENTER_Y

    sun_border_x = sun_x + sun_radius
    sun = get_circle(sun_x, sun_y, sun_radius, "yellow")

    return sun, sun_border_x


def clear_window():
    rectangle = gr.Rectangle(gr.Point(0, 0), gr.Point(SIZE_X, SIZE_Y))
    rectangle.setFill('black')
    rectangle.draw(window)


def update_acceleration(ball_coords, center_coords):
    diff = sub(ball_coords, center_coords)
    distance_2 = (diff.x ** 2 + diff.y ** 2) ** (3/2)

    G = 2000

    return gr.Point(-diff.x*G/distance_2, -diff.y*G/distance_2)


window = gr.GraphWin("Solar System", SIZE_X, SIZE_Y)

sun, sun_border_x = get_sun()
    

mercury, mercury_border_x = get_planet(SIZE_X / 500 * 5, sun_border_x, "white")

venus, venus_border_x = get_planet(SIZE_X / 500 * 8, mercury_border_x, "#ffe6cc")

earth, earth_border_x = get_planet(SIZE_X / 500 * 10, venus_border_x, "#33bbff")

mars, mars_border_x = get_planet(SIZE_X / 500 * 7, earth_border_x, "#cc4400")



clear_window()

sun.draw(window)
mercury.draw(window)



while True:

    mercury.move(1, 1)

    gr.time.sleep(0.02)


#window.getMouse()
#window.close()

'''
jupiter, jupiter_border_x = get_planet(71.49 / 4, mars_border_x, "#ffccb3")

saturn, saturn_border_x = get_planet(60.27 / 4, jupiter_border_x, "#997a00")

uranus, uranus_border_x = get_planet(25.56 / 4, saturn_border_x, "#004d99")

neptune, neptune_border_x = get_planet(24.76 / 4, uranus_border_x, "#002080")
'''

'''
    venus.draw(window)
    earth.draw(window)
    mars.draw(window)
    jupiter.draw(window)
    saturn.draw(window)
    uranus.draw(window)
    neptune.draw(window)
'''