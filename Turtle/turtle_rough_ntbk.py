from turtle import Turtle, Screen
import os, random

os.system('cls')

def random_turtle_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r, g, b)


def square():

    t = Turtle()
    s = Screen()

    t.screen.title('Turtle demo: DRAW A SQUARE')
    t.shape('turtle')
    t.color("red")

    for _ in range(4):
        t.fd(100)
        if t.pos() == (0.00, 0.00):
            print("turtle is at the")
        t.left(90)

    

    s.exitonclick()
    # t.screen.mainloop()

# square()

'''
    t1.screen.bgcolor("black")
    t1 = Turtle()
    t1.shape('turtle')
    t1.color("black")
    t1.teleport(-50,-50)
'''

def dashed_line():

    t = Turtle()
    s = Screen()
    t.shape('turtle')
    s.colormode(255)
    t.color(47,79,79)
    while t.pos() <= (200,0):
        t.fd(10)
        t.penup()
        t.fd(10)
        t.pendown()

    s.exitonclick()

# dashed_line()

def shapes():

    t = Turtle()
    s = Screen()

    s.colormode(255)
    t.speed("fastest")

    def left_right():
        pass #return func for func in [t.left, t.right]

    for side in range(3, 11):
        angle = 360 / side
        t.color(random_turtle_color())

        for function in [t.left, t.right]:
            for _ in range(side):
                t.fd(100)
                function(angle)
    
    s.exitonclick()

# shapes()

def random_walk():

    t = Turtle()
    s = Screen()

    s.colormode(255)
    angles = [0, 90, 180, 270]
    t.width(10)
    t.speed("fastest")
    t.hideturtle()

    for _ in range(100):
        
        t.color(random_turtle_color())
        angle = random.choice(angles)
        t.fd(50)
        t.setheading(angle)
    

    s.exitonclick()

# random_walk()

def spirograph(step):

    t = Turtle()
    s = Screen()

    s.colormode(255)
    t.speed('fastest')

    for angle in range(0, 365, step):
        t.color(random_turtle_color())
        t.circle(100)
        t.setheading(angle)
    
    s.exitonclick()

# spirograph(3)

import colorgram
filename = 'hirst_painting.jpeg'
filepath = 'C:\\Users\Avinash_Anand\\OneDrive - Dell Technologies\\Documents\\Learning\\Python\\Udemy\\Notes & Learnings\\Python-Coding\\Turtle\\'
colors = colorgram.extract(f"{filepath}{filename}", 15)
color_palette = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]
print(color_palette)

def hirst_painting():

    t = Turtle()
    s = Screen()
    t.hideturtle()
    t.shape("turtle")

    s.colormode(255)
    t.speed("fastest")
    t.penup()
    t.setposition(-125, -100)

    for _ in range(11):
        for _ in range(11):
            t.dot(10, random.choice(color_palette))
            t.fd(20)

        t.left(90)
        t.fd(20)
        t.left(90)
        t.setx(-125)
        t.setheading(0)

    s.exitonclick()

hirst_painting()