from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape('turtle')
timmy.color('coral')

screen = Screen()

# DRAW A SQUARE
for _ in range(4):
    timmy.fd(100)
    timmy.left(90)

screen.exitonclick()