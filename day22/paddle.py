from turtle import Turtle

class Paddle:
    def __init__(self):
        self.width = 5
        self.height = 1
        self.paddle = None
        self.up = True


    def create_paddle(self, start_x, start_y): #tehdään tämä paremmin vielä
        self.paddle = Turtle("square")
        self.paddle.hideturtle()
        self.paddle.penup()
        self.paddle.color("white")
        self.paddle.turtlesize(self.width, self.height)
        self.paddle.goto(start_x, start_y)
        self.paddle.showturtle()
    
    def move_up(self):
        if self.paddle:
            new_y = self.paddle.ycor() + 20 
            self.paddle.goto(self.paddle.xcor(), new_y)
    def move_down(self):
        if self.paddle:
            new_y = self.paddle.ycor() - 20  
            self.paddle.goto(self.paddle.xcor(), new_y)
    
    def automated_movement(self):
        if self.up:
            new_y = self.paddle.ycor() + 10 
            self.paddle.goto(self.paddle.xcor(), new_y)
            if self.paddle.ycor() >= 280:
                self.up = False
        elif not self.up:
            new_y = self.paddle.ycor() - 10  
            self.paddle.goto(self.paddle.xcor(), new_y)
            if self.paddle.ycor() <= -280:
                self.up = True


