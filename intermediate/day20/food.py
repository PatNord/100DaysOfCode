from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5,0.5)
        self.color("yellow")
        self.speed("fastest")
        self.new_location()

    
    def new_location(self):
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)

        self.goto(x,y)

    
