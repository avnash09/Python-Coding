from turtle import Turtle, Screen
import random, os
import colorgram

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

def get_rgb():

    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    return (r, g, b)

t = Turtle()
s = Screen()

t.speed("fastest")
s.colormode(255)
t.penup()
#t.hideturtle()
#print(start_xcor, ',', start_ycor)

def quadrilateral():

    dots = 100
    rows = 5
    columns = int(dots / rows)
    dot_size = 20
    step_size = dot_size * 1.5
    dots_each_row = int(dots / rows)
    dots_each_col = int(dots / columns)

    start_xcor = -1 * ((step_size) * dots_each_row/2) + (step_size/2)
    start_ycor = -1 * ((step_size) * dots_each_col/2) + (step_size/2)

    t.setpos(start_xcor, start_ycor)

    for y in range(1, dots + 1):
        t.dot(dot_size, get_rgb())
        t.forward(step_size)

        if y % dots_each_row == 0:
            #print(y, t.pos())
            t.setheading(90)
            t.forward(step_size)
            t.setheading(0)
            t.backward(step_size * dots_each_row)

def triangle():
    
    rows = 15
    dot_size = 20
    step_size = dot_size * 1.5

    start_xcor = -1 * ((step_size) * rows) / 2
    start_ycor = -1 * ((step_size) * rows) / 2

    t.setpos(start_xcor, start_ycor)
    
    for i in range(rows+1, 0, -1):
        
        for _ in range(1, i):
            t.dot(dot_size, get_rgb())
            t.forward(step_size)
        
        t.setheading(90)
        t.forward(step_size)
        t.setheading(0)
        t.backward((step_size)*(i-1))
        t.forward(step_size/2)

quadrilateral()

s.exitonclick()