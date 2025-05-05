from turtle import Turtle, Screen
import random, os
import colorgram

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

# Extract colors from an image
# print(os.getcwd())
# colors = colorgram.extract('hirst_painting.jpeg', 25)
# rgb_colors = []

# for color in colors:
#     r = color.rgb.r #if color.rgb.r < 240 else 0
#     g = color.rgb.g #if color.rgb.g < 240 else 0
#     b = color.rgb.b #if color.rgb.g < 240 else 0
#     color_tuple = (r,g,b)
#     rgb_colors.append(color_tuple)

# print(rgb_colors)

t = Turtle()
s = Screen()

t.speed("fastest")
s.colormode(255)

def get_rgb():

    red = random.randint(0,255)
    blue = random.randint(0,255)
    green = random.randint(0,255)

    return (red, blue, green)

colors = [(211, 210, 210), (189, 167, 121), (57, 90, 111), (113, 43, 35), (163, 89, 64), (210, 212, 214), (208, 211, 208), (211, 209, 210), (64, 43, 43), (171, 183, 170), (136, 149, 69), (127, 160, 172), (101, 79, 89), (83, 133, 108), (108, 39, 44), (39, 61, 47), (45, 40, 41), (211, 196, 124), (174, 150, 152), (36, 71, 88), (179, 106, 80), (36, 67, 84), (207, 185, 181), (99, 140, 119), (184, 198, 181)]

t.penup()
t.hideturtle()
start_point = (-225, -225)
t.setpos(start_point)

for y in range(50, 500, 50):
    for _ in range(10):
        t.dot(20,random.choice(colors))
        t.forward(50)

    new_xcor = start_point[0]
    new_ycor = start_point[1] + y
    t.setpos(new_xcor, new_ycor)

s.exitonclick()