import turtle
turtle.bgcolor("skyblue")
turtle.setup(800,800)
pen = turtle.Turtle()
pen.pensize(5)
pen.color("orange")

#square
pen.fillcolor("blue")
pen.begin_fill()
pen.forward(50)
pen.left(90)
pen.forward(50)
pen.left(90)
pen.forward(50)
pen.left(90)
pen.forward(50)
pen.left(90)
pen.end_fill()

pen.up()
pen.setpos(-200, 0)
pen.down()
pen.setheading(0)

#triangle
pen.forward(50)
pen.right(120)
pen.forward(50)
pen.right(120)
pen.forward(50)
pen.right(120)

#circle
pen.up()
pen.setpos(100, -200)
pen.down()
pen.setheading(0)
pen.color("purple")
pen.begin_fill()
pen.circle(40)
pen.end_fill()

turtle.done()