from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1

    def score_board(self):
        self.penup()
        self.goto(-290, 260)
        self.hideturtle()
        self.color("white")
        self.write(f"Level:{self.level}", align="left", font=("Courier", 24, "normal"))

    def level_up(self):
        self.level += 1
        self.clear()
        self.score_board()

    def game_over(self):
        self.penup()
        self.hideturtle()
        self. goto(0,0)
        self.color("white")
        self.write("Game Over!", align="center", font=("Courier", 24, "normal"))
