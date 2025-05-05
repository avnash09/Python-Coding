from turtle import Turtle, Screen
import random

# Get the underlying TKinter window and force it to be on top
# canvas = screen.getcanvas()
# canvas.winfo_toplevel().attributes("-topmost", 1)

timmy = Turtle()
timmy.shape('turtle')
timmy.color('coral')

screen = Screen()
screen.colormode(255)

# DRAW A SQUARE
# for _ in range(4):
#     timmy.fd(100)
#     timmy.left(90)

#DRAW A DASHED LINE
# for _ in range(15):
#     timmy.fd(5)
#     timmy.penup()
#     timmy.fd(5)
#     timmy.pendown()

# DRAW A TRIANGLE, SQAURE, PENTAGON, HEXAGON, HEPTAGON, OCTAGON, NONAGON, DECAGON

def draw(sides):
    
    angle = 360 / sides

    r,g,b = turtle_color()

    timmy.pencolor(r,g,b)

    for _ in range(sides):
        timmy.fd(100)
        timmy.right(angle)

def turtle_color():

    red = random.randint(50,255)
    blue = random.randint(50,255)
    green = random.randint(50,255)

    return (red, blue, green)

for sides in range(3, 11):
    draw(sides)

screen.exitonclick()
# canvas.winfo_toplevel().attributes("-topmost", 0)  # Reset to normal