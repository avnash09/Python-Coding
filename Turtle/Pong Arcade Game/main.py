from turtle import Turtle, Screen
import os, random, time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

clear_terminal()

STARTING_POSITIONS = {'r_start_pos': (350, 0), 'l_start_pos': (-350, 0)}

s = Screen()
s.bgcolor('black')
s.setup(width=800, height=600)
s.title("Bong: The Arcade game")
s.tracer(0)

r_paddle = Paddle(STARTING_POSITIONS['r_start_pos'])
l_paddle = Paddle(STARTING_POSITIONS['l_start_pos'])
ball = Ball()
scoreboard = Scoreboard()

s.listen()
s.onkeypress(r_paddle.go_up, "Up")
s.onkeypress(r_paddle.go_down, "Down")
s.onkeypress(l_paddle.go_up, "w")
s.onkeypress(l_paddle.go_down, "s")

game_on = True

while game_on:

    s.update()
    ball.move()
    time.sleep(ball.move_speed)

    #Detect collision with top or bottom wall
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        print("T/B wall collision")
        ball.bounce_y()

    #Detect right paddle miss
    if ball.xcor() >= 380:
        ball.reset_position()
        print("Right wall collision")
        scoreboard.l_point()

    #Detect left paddle miss
    if ball.xcor() <= -380:
        ball.reset_position()
        print("Left wall collision")
        scoreboard.r_point()

    #Detect collision with left or right paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 340) or (ball.distance(l_paddle) < 50 and ball.xcor() < -340):
        ball.bounce_x()
        print("Paddle bounce")

s.exitonclick()
