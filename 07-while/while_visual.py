# draw 10 randomly spaced circles, 
# of various colors

import random
import turtle
turtle.bgcolor("skyblue")
turtle.setup(800,800)
pen = turtle.Turtle()
pen.pensize(5)
pen.speed(0)
turtle.colormode(255)

count = 1

numDots = turtle.numinput("Dots", "How many polka-dots: ")

while count < numDots:
    count += 1
    
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    pen.color(r,g,b)
    
    x = random.randint(-turtle.window_width()//2, turtle.window_width()//2)
    y = random.randint(-turtle.window_height()//2, turtle.window_height()//2)
    
    pen.up()
    pen.setpos(x,y)
    pen.down()
    
    pen.begin_fill()
    pen.circle(50)
    pen.end_fill()

turtle.done()