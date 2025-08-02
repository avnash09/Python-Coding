from turtle import Turtle, Screen
import os, random

os.system('cls') #clear screen

t = Turtle()
s = Screen()
t.speed('fastest')
t.pensize(1)

step_size = 20

def up():
    t.forward(step_size)

def down(): 
    t.backward(step_size)

def left():
    t.left(10)

def right():
    t.right(10)

def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()


s.onkey(up, "w")
s.onkey(down, "s")
s.onkey(left, "a")
s.onkey(right, "d")
s.onkey(clear, "c")
s.listen()

s.exitonclick()