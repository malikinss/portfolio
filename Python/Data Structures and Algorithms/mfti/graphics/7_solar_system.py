import graphics as gr


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
    
    sun_radius = 696.34 / 4
    sun_x = CENTER_X
    sun_y = CENTER_Y

    sun_border_x = sun_x + sun_radius
    sun = get_circle(sun_x, sun_y, sun_radius, "yellow")

    return sun, sun_border_x




SIZE_X = 1500
SIZE_Y = 1500

CENTER_X = SIZE_X / 2
CENTER_Y = SIZE_Y / 2

window = gr.GraphWin("Solar System", SIZE_X, SIZE_Y)



sun, sun_border_x = get_sun()


mercury, mercury_border_x = get_planet(2.44 / 4, sun_border_x, "#7575a3")

venus, venus_border_x = get_planet(6.052 / 4, mercury_border_x, "#ffe6cc")

earth, earth_border_x = get_planet(6.378 / 4, venus_border_x, "#33bbff")

mars, mars_border_x = get_planet(3.397 / 4, earth_border_x, "#cc4400")

jupiter, jupiter_border_x = get_planet(71.49 / 4, mars_border_x, "#ffccb3")

saturn, saturn_border_x = get_planet(60.27 / 4, jupiter_border_x, "#997a00")

uranus, uranus_border_x = get_planet(25.56 / 4, saturn_border_x, "#004d99")

neptune, neptune_border_x = get_planet(24.76 / 4, uranus_border_x, "#002080")

#draw
sun.draw(window)
mercury.draw(window)
venus.draw(window)
earth.draw(window)
mars.draw(window)
jupiter.draw(window)
saturn.draw(window)
uranus.draw(window)
neptune.draw(window)


window.getMouse()
window.close()

