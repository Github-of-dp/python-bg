# importing turtle module
import turtle
# size
n = 100
turtle.pensize(2)
turtle.speed(0)
screen = turtle.Screen()
screen.bgcolor("orange")
# loop to draw a side
def start_drawing(x, y):
    turtle.pendown()
    for i in range(n * 3):
            turtle.color("purple")
            turtle.forward(i * 10)
            turtle.right(122)

# Start When Clicked
screen.onscreenclick(start_drawing)
