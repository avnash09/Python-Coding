from turtle import Turtle, Screen
import random

COLORS = ["red", "blue", "green", "magenta", "orange", "purple", "brown", "LightSeaGreen", "LightSkyBlue"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):

    car_speed = STARTING_MOVE_DISTANCE

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_len=2, stretch_wid=0.8)
        random_color = random.choice(COLORS)
        self.color(random_color)
        self.penup()
        # self.goto(300, random.randint(-250, 250))
        random_y = random.choice(range(-220, 220, 20))
        self.goto(300, random_y)

    def move(self):
        self.backward(self.car_speed)
    
    @classmethod
    def level_up(cls):
        cls.car_speed += MOVE_INCREMENT


if __name__ == '__main__':
    import time
    s = Screen()
    s.setup(width=600, height=600)
    s.tracer(0)

    cars = []
    
    while True:

        time.sleep(0.1)
        s.update()
        
        if random.randint(1,10) <= 3:
            car = CarManager()
            cars.append(car)

        for car in cars:
            car.move()
            if car.xcor() <= -280:
                car.hideturtle()
                cars.remove(car)


    s.exitonclick()
