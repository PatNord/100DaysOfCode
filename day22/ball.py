from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.width = 20
        self.height = 20
        self.xpos = 0
        self.ypos = 0

