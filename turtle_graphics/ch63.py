# Draw three squares in a row with a gap between each. Fill them using three different colours.

import turtle

turtle.pendown()
turtle.color('black', 'red')
turtle.begin_fill()
for i in range(0, 4):
    turtle.forward(100)
    turtle.right(90)
turtle.penup()
turtle.end_fill()
turtle.forward(200)

turtle.pendown()
turtle.begin_fill()
turtle.color('black', 'yellow')
for i in range(0, 4):
    turtle.forward(100)
    turtle.right(90)
turtle.penup()
turtle.end_fill()
turtle.forward(200)

turtle.pendown()
turtle.begin_fill()
turtle.color('black', 'blue')
for i in range(0, 4):
    turtle.forward(100)
    turtle.right(90)
turtle.penup()
turtle.end_fill()


turtle.exitonclick()
