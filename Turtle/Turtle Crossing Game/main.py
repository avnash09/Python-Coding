import time, os, random
from turtle import Turtle, Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard, FinishLine

def clear_terminal():
    if os.name == 'nt': os.system('cls')
    else: os.system('clear')

clear_terminal()

s = Screen()
s.setup(width=600, height=600)
s.tracer(0)

player = Player()
scoreboard = Scoreboard()
finish_line = FinishLine()

s.listen()
s.onkey(player.move_forward, "Up")
s.onkey(player.move_backward, "Down")

cars = []
game_on = True

while game_on:

    time.sleep(0.1)
    s.update()

    #create cars randomly
    if random.randint(1,10) == 1:
        new_car = CarManager()
        cars.append(new_car)

    #move cars
    for car in cars:
        car.move()
        if car.xcor() <= -320:
            car.hideturtle()
            cars.remove(car)

    #Detect player reaching finish line
    if player.has_finished():
        scoreboard.increase_level()
        player.reset_position()
        for car in cars:
            car.level_up()

    #Detect collision with car
    for car in cars:
        if car.distance(player) < 20 and car.ycor() - player.ycor() < 10:
            game_on = False
            scoreboard.game_over()   
    
s.exitonclick()