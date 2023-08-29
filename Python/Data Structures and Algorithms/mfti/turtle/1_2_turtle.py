# Write your name using Python

import turtle

turtle.shape('turtle')

# "S" letter
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)

# white space
turtle.penup()
turtle.forward(20)
turtle.pendown()

# "A" letter
turtle.right(90)
turtle.forward(100)

turtle.penup()
turtle.backward(100)
turtle.left(90)
turtle.pendown()

turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)

turtle.penup()
turtle.backward(50)
turtle.left(90)
turtle.pendown()

turtle.forward(50)
turtle.left(90)


# white space
turtle.penup()
turtle.forward(20)
turtle.pendown()


# "M" letter
turtle.left(90)
turtle.forward(100)

turtle.right(135)
turtle.forward(35.5)

turtle.left(90)
turtle.forward(35.5)

turtle.right(135)
turtle.forward(100)