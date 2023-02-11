import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("grey")

# Create a turtle
turtle = turtle.Turtle()
turtle.speed(0)
turtle.pensize(5)

# Draw a spiral
def start_drawing(x, y):
    turtle.pendown()
    for i in range(800):
        turtle.pencolor(random.random(), random.random(), random.random())
        turtle.forward(5 * i)
        turtle.right(170)

# Start When Clicked
screen.onscreenclick(start_drawing)
