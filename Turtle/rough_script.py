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
t.penup()
dots = 100 #input("Enter the number of dots: ")
rows = 10
dot_size = 30
step_size = dot_size * 1.5
dots_each_row = dots / rows
#home_xcor = -1 * ((500 / dots_each_row) + (dot_size + step_size))
home_xcor = -1 * ((step_size) * dots_each_row/2)
home_ycor = -1 * ((step_size) * dots_each_row/2)
print(home_xcor, ',', home_ycor)
t.setpos(home_xcor, home_ycor)

def get_rgb():

    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    return (r, g, b)

for y in range(1, dots + 1):
    t.dot(dot_size, 'coral')
    t.forward(step_size)

    if y % 10 == 0:
        #print(y, t.pos())
        t.setheading(90)
        t.forward(step_size)
        t.setheading(0)
        t.backward((step_size) * dots_each_row)



s.exitonclick()