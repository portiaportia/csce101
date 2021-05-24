import turtle
turtle.bgcolor("skyblue")
turtle.setup(800,800)
pen = turtle.Turtle()
pen.pensize(5)
pen.fillcolor("aquamarine")

# draw the house base
pen.up()
pen.setpos(-100, -100)
pen.down()

pen.begin_fill()
for i in range(4):
    pen.forward(200)
    pen.left(90)
pen.end_fill()

# draw the door
pen.up()
pen.setpos(-25, -100)
pen.down()

pen.fillcolor("hot pink")
pen.begin_fill()
for i in range(4):
    if i % 2 == 0:      # if i is even
        pen.forward(50)
    else:               # for i odd
        pen.forward(100)
    pen.left(90)
pen.end_fill()

# draw the roof
pen.up()
pen.setpos(-120, 100)
pen.down()

pen.fillcolor("hot pink")
pen.begin_fill()
for i in range(3):
    pen.forward(240)
    pen.left(120)
pen.end_fill()

turtle.done()