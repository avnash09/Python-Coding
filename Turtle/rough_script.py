from turtle import Turtle, Screen
import random, os
import colorgram

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

t = Turtle()
s = Screen()

t.speed("fastest")
s.colormode(255)
dots = 100 #input("Enter the number of dots: ")
rows = 10
dot_size = 10
step_size = dot_size * 2
dots_each_row = dots / rows
home_xcor = -1 * (500 / dots) * (dots_each_row + step_size)
t.setpos(home_xcor, 0)

for y in range(1, dots + 1):
    t.dot(dot_size, 'black')
    t.forward(step_size)

    if y % 10 == 0:
        t.setheading(90)
        t.forward(step_size)
        t.setheading(0)
        t.backward((step_size) * dots_each_row)



s.exitonclick()