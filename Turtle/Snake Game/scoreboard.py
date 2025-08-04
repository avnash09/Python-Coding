from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 18, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.score = 0
        self.high_score = 0
        self.penup()
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.goto(0, 270)
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", True, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.home()
        self.write("Game over.", True, align=ALIGNMENT, font=FONT)

    def reset_all_scores(self):
        self.high_score = 0
        self.score = 0

    def reset(self):
        self.score = 0

    def update_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
