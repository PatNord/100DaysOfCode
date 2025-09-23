from turtle import Turtle, colormode
import random

colormode(255)

class Car(Turtle):
    car_speed = 5
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.randint(0, 255),random.randint(0, 255), random.randint(0, 255))
        self.goto(400, random.randint(-350, 350))
        self.showturtle()
    
    def move(self):
        new_x = self.xcor() - Car.car_speed
        self.goto(new_x, self.ycor())

    @classmethod
    def increase_difficulty(cls):
        cls.car_speed += 5
