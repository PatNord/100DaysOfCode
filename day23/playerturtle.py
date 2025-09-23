from turtle import Turtle

class Playerturtle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.hideturtle()
        self.penup()
        self.seth(90)
        self.goto(0, -350)
        self.showturtle()

    def move_up(self):
        new_y = self.ycor() + 10
        self.goto(self.xcor(), new_y)
    def move_down(self):
        new_y = self.ycor() - 10
        self.goto(self.xcor(), new_y)
    def move_left(self):
        new_x = self.xcor() - 10
        self.goto(new_x, self.ycor())
    def move_right(self):
        new_x = self.xcor() + 10
        self.goto(new_x, self.ycor())

    def reset_position(self):
        self.goto(0, -350)