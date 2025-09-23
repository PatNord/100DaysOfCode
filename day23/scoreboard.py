from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 350)
        self.write(self.score, align="center", font=("Courier", 20, "normal"))

    def point(self):
        self.score += 1
        self.update_scoreboard()