from turtle import Turtle
import os

ALIGNMENT = "center"
FONT = ("Courier", 18, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.score = 0
        self.filepath = os.getcwd() + "\\Turtle\\Snake Game\\"
        self.filename = 'data_file.txt'
        self.high_score = self.get_high_score()
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
            with open(self.filepath + self.filename, mode='w') as file:
                file.write(str(self.high_score))

    def get_high_score(self):
        with open(self.filepath + self.filename, mode='r') as file:
            high_score = file.read()
            return int(high_score)

if __name__ == '__main__':
        
    s = Scoreboard()
    s.get_high_score()
