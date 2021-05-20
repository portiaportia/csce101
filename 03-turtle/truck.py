import turtle
turtle.bgcolor("skyblue")
turtle.setup(800,800)
pen = turtle.Turtle()
pen.pensize(5)
pen.speed(0)
pen.color("black")
pen.fillcolor("red")

pen.up()
pen.setpos(-100, 0)
pen.down()

#draw truck bed
pen.begin_fill()
pen.forward(200)
pen.left(90)
pen.forward(50)
pen.left(90)
pen.forward(200)
pen.left(90)
pen.forward(50)
pen.left(90)
pen.end_fill()

#draw truck cab
pen.up()
pen.setpos(20,50)
pen.down()
pen.begin_fill()
pen.forward(80)
pen.left(90)
pen.forward(40)
pen.left(90)
pen.forward(80)
pen.left(90)
pen.forward(40)
pen.left(90)
pen.end_fill()

# draw back wheel
pen.begin_fill()
pen.up()
pen.setpos(-50, -20)
pen.down()
pen.fillcolor("black")
pen.circle(20)
pen.end_fill()

# draw front wheel
pen.begin_fill()
pen.up()
pen.setpos(50, -20)
pen.down()
pen.fillcolor("black")
pen.circle(20)
pen.end_fill()

# draw window
pen.begin_fill()
pen.up()
pen.setpos(50, 50)
pen.down()
pen.fillcolor("white")
pen.forward(20)
pen.left(90)
pen.forward(20)
pen.left(90)
pen.forward(20)
pen.left(90)
pen.forward(20)
pen.left(90)
pen.end_fill()

# sun
pen.up()
pen.setpos(-250,230)
pen.down()
pen.color("yellow")
pen.begin_fill()
pen.circle(50)
pen.end_fill()

# star
pen.up()
pen.setpos(-100,230)
pen.down()
pen.color("yellow")
pen.begin_fill()
pen.setheading(0)
pen.forward(100)
pen.left(144)
pen.forward(100)
pen.left(144)
pen.forward(100)
pen.left(144)
pen.forward(100)
pen.left(144)
pen.forward(100)
pen.end_fill()

#christmas tree
pen.up()
pen.setpos(250, -50)
pen.down()
pen.color("black")
pen.fillcolor("brown")
pen.setheading(0)

# stump
pen.begin_fill()
pen.forward(20)
pen.left(90)
pen.forward(20)
pen.left(90)
pen.forward(20)
pen.left(90)
pen.forward(20)
pen.left(90)
pen.end_fill()

pen.up()
pen.setpos(235, -30)
pen.down()
pen.fillcolor("green")
pen.begin_fill()
pen.forward(50)
pen.left(120)
pen.forward(50)
pen.left(120)
pen.forward(50)
pen.left(120)
pen.end_fill()

turtle.done()