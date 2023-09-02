# connecting the library under alias gr
import graphics as gr

# Initialization of a window with the name "Russian game" and a size of 400x400 pixels
window = gr.GraphWin("Russian game", 400, 400)

# Create a circle with radius 10 and center coordinates (50, 50)
my_circle = gr.Circle(gr.Point(50, 50), 10)

# Create a line with ends at points (2, 4) and (4, 8)
my_line = gr.Line(gr.Point(2, 4), gr.Point(4, 8))

# Creating a rectangle whose diagonal is a segment with ends at points (2, 4) and (4, 8)
my_rectangle = gr.Rectangle(gr.Point(2, 4), gr.Point(4, 8))

# Drawing primitives in the window "window"
my_circle.draw(window)
my_line.draw(window)
my_rectangle.draw(window)

#  Waiting for a mouse button to be pressed on the window.
window.getMouse()

#  After we have completed all the necessary operations, the window should be closed.
window.close()