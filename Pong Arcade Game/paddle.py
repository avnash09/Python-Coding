from turtle import Turtle

MOVE_DISTANCE = 30

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.setheading(90)
        self.goto(position)

    #go up function
    def go_up(self):
        # paddle.setheading(90)
        self.forward(MOVE_DISTANCE)

    #go down function
    def go_down(self):
        # paddle.setheading(270)
        self.backward(MOVE_DISTANCE)
        