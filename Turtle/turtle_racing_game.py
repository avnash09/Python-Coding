from turtle import Turtle, Screen
import os, random

os.system('cls')

def draw_finishing_line():
    t = Turtle()
    t.speed("fastest")
    t.penup()
    t.hideturtle()
    # t.goto(100, 50)
    t.teleport(350, -(h/2))
    t.setheading(90)  # Point turtle straight up (90°)

    dash_length = 10
    gap_length = 5
    line_length = h  # Total height of the canvas
    num_dashes = line_length // (dash_length + gap_length)

    for _ in range(int(num_dashes)):
        t.pendown()
        t.forward(dash_length)
        t.penup()
        t.forward(gap_length)

is_race_on = False
s = Screen()
w=800
h=500
s.setup(width=w, height=h)
turtle_colors = ["red", "blue", "green", "magenta", "orange", "purple"]
user_choice = int(s.numinput(title="Make your bet", 
                        # prompt=f"Predict a winner\n1. {turtle_colors[0]}\n2. {turtle_colors[1]}\n3. {turtle_colors[2]}\n4. {turtle_colors[3]}\n5. {turtle_colors[4]}", 
                        prompt="Predict a winner: \n" + '\n'.join(f"{i+1}. {color}" for i, color in enumerate(turtle_colors)),
                        default=0, minval=1, maxval=len(turtle_colors)))
user_bet = turtle_colors[user_choice - 1]
print(user_choice,user_bet)

start_pos = -1 * int((h * 2)/len(turtle_colors))
print(start_pos)

draw_finishing_line()

turtles = {}
for turtle_color in turtle_colors:
    turtles[turtle_color] = Turtle(shape="turtle")
    # turtles[color].shape("turtle")
    turtles[turtle_color].color(turtle_color)
    turtles[turtle_color].penup()
    turtle_index = turtle_colors.index(turtle_color)
    turtles[turtle_color].teleport(-350, start_pos + (turtle_index * (h-100)/len(turtle_colors)) )

if user_bet:
    is_race_on = True

while is_race_on:

    for color, turtle in turtles.items():
        distance = random.randint(1, 10)
        turtle.fd(distance)
        if turtle.xcor() > 350:
            if user_bet == color:
                print(f"You've won! The {color} turtle won the race.")
            else:
                print(f"You've lost, The {color} turtle won the race.")
            is_race_on = False
            break



s.exitonclick()