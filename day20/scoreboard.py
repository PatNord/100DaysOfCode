from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.goto(0, 260)
        self.color("white")
        self.score = 0
        self.write(arg=f"score: {self.score}", align="center", font=('Arial', 20, 'normal'))
    
    def update_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f"score: {self.score}", align="center", font=('Arial', 20, 'normal'))
    
    def you_lost(self):
        self.penup()
        self.clear()
        self.goto(0,0)
        self.write(arg=f"You lost!", align="center", font=('Arial', 50, 'normal'))
        self.goto(0,-30)
        self.write(arg=f"Final score {self.score}", align="center",font=('Arial', 25, 'normal'))