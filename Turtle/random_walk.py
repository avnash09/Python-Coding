from turtle import Turtle, Screen
import random

t = Turtle()
s = Screen()

t.pensize(10)
t.speed("fastest")

angles = [0, 90, 180, 270]

colors = [
    "red",
    "blue",
    "green",
    "yellow",
    "orange",
    "purple",
    "pink",
    "cyan",
    "magenta",
    "lime",
    "gold",
    "turquoise",
    "navy",
    "maroon",
    "olive",
    "teal",
    "violet",
    "coral",
    "orchid",
    "indigo"
]

for _ in range(100):

    random_color = random.choice(colors)
    random_angle = random.choice(angles)
    t.color(random_color)

    t.fd(30)
    t.setheading(random_angle)

s.exitonclick()