import os, random, time
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

SNAKE_SPEED = 0.1

def clear_terminal():
    if os.name == 'nt': #Windows
        os.system('cls')
    else:   #Linus/MacOS
        os.system('clear')
        
clear_terminal()

s = Screen()
s.setup(width=600, height=600)
s.bgcolor('black')
s.title('My Snake Game')
s.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()


s.listen()
s.onkey(snake.up, "Up")
s.onkey(snake.down, "Down")
s.onkey(snake.left, "Left")
s.onkey(snake.right, "Right")

is_game_on = True
while is_game_on:
    s.update()
    time.sleep(SNAKE_SPEED)

    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()

    #Detect collision with wall
    if snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        print("Wall collision")
        # score.game_over()
        # is_game_on = False
        score.update_high_score()
        score.update_scoreboard()
        score.reset()
        snake.reset()

    #Detect collision with tail
    #if head collides with any segment in the tail, trigger game_over()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            print(snake.segments.index(segment))
            print("Tail collision")
            # score.game_over()
            # is_game_on = False
            score.update_high_score()
            score.update_scoreboard()
            score.reset()
            snake.reset()

s.exitonclick()