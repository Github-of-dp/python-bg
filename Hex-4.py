import turtle
screen = turtle.Screen()
turtle.speed(0)
turtle.setup(1000,1000)
turtle.pensize(3)
turtle.hideturtle()
screen.bgcolor("black")

def start_drawing(x, y):
    turtle.pendown()
    for i in range(10,780,3):
            turtle.pencolor("green")
            turtle.fd(i)
            turtle.left(59)

screen.onscreenclick(start_drawing)
