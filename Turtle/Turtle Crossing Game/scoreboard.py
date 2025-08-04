from turtle import Turtle, Screen

FONT = ("Courier", 14, 'normal')
POSITION = (-230, 260)

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.goto(POSITION)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def game_over(self):
        self.home()
        self.write(f"Game over.", True, align="center", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

class FinishLine(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('black')
        self.goto(-300, POSITION[1])
        while self.xcor() <= 300:
            self.draw_finish_line()
    
    def draw_finish_line(self):
        self.pendown()
        self.forward(10)
        self.penup()
        self.forward(5)


if __name__ == '__main__':
    screen = Screen()
    screen.setup(600, 600)
    screen.tracer(0)

    s = Scoreboard()
    s.increase_level()

    screen.update()
    screen.exitonclick()