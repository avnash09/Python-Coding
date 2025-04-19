from turtle import Turtle, Screen
import random

t = Turtle()
s = Screen()

t.speed("fastest")
s.colormode(255)

def get_rgb():

    red = random.randint(0,255)
    blue = random.randint(0,255)
    green = random.randint(0,255)

    return (red, blue, green)

for tilt_angle in range(0,360,3):

    r,g,b = get_rgb()
    t.color((r,g,b))
    t.circle(100)
    t.setheading(tilt_angle)

t.circle(100,None,720)

s.exitonclick()