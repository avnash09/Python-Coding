from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape('turtle')
timmy.color('coral')

screen = Screen()

#DRAW A DASHED LINE
for _ in range(15):
    timmy.fd(5)
    timmy.penup()
    timmy.fd(5)
    timmy.pendown()

screen.exitonclick()