import turtle
turtle.bgcolor("skyblue")
turtle.setup(800,800)
pen = turtle.Turtle()
pen.pensize(5)

color = turtle.textinput("Colors", "Enter Color").strip().lower()
size = turtle.numinput("Colors", "Enter size")
shape = turtle.textinput("Shape", "Enter Shape").strip().lower()

pen.up()
pen.setpos(0, -size)
pen.down()
pen.fillcolor(color)
pen.begin_fill()

if shape == "circle":
    pen.circle(size*2)
elif shape == "square":
    pen.forward(size * 2)
    pen.left(90)
    pen.forward(size * 2)
    pen.left(90)
    pen.forward(size * 2)
    pen.left(90)
    pen.forward(size * 2)
    pen.left(90)
else:
    turtle.write("Sorry thats not a shape", font=("Arial", 16, "normal")) 
pen.end_fill()


turtle.done()