from turtle import Turtle, Screen

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 30 #5
FINISH_LINE_Y = 250

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.penup()
        self.setheading(90)
        self.reset_position()

    def move_forward(self):
        self.forward(MOVE_DISTANCE)

    def move_backward(self):
        self.backward(MOVE_DISTANCE)

    def reset_position(self):
        self.goto(STARTING_POSITION)

    def has_finished(self):
        return self.ycor() >= FINISH_LINE_Y


if __name__ == '__main__':

    p = Player()
    p.speed('fastest')
    s = Screen()

    print('Current file')

    s.exitonclick()