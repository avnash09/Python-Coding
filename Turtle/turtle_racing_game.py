from turtle import Turtle, Screen
import os, random

os.system('cls')

is_race_on = False
s = Screen()
s.setup(width=800, height=500)
turtle_colors = ["red", "blue", "green", "magenta", "orange", "purple"]
user_choice = int(s.numinput(title="Make your bet", 
                          prompt=f"Predict a winner\n1. {turtle_colors[0]}\n2. {turtle_colors[1]}\n3. {turtle_colors[2]}\n4. {turtle_colors[3]}\n5. {turtle_colors[4]}", 
                          default=0, minval=1, maxval=5))
user_bet = turtle_colors[user_choice - 1]
print(user_choice,user_bet)

turtles = {}
for color in turtle_colors:
    turtles[color] = Turtle(shape="turtle")
    # turtles[color].shape("turtle")
    turtles[color].color(color)
    turtles[color].penup()
    turtle_index = turtle_colors.index(color)
    turtles[color].teleport(-350, -100 + (turtle_index * 50) )

if user_bet:
    is_race_on = True

while is_race_on:

    for color, turtle in turtles.items():
        distance = random.randint(1, 10)
        turtle.fd(distance)
        if turtle.xcor() >= 350:
            if user_bet.lower() == color:
                print(f"You've won! The {color} turtle won the race.")
            else:
                print(f"You've lost, The {color} turtle won the race.")
            is_race_on = False
            break



s.exitonclick()