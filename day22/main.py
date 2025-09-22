from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
game_is_on = True
screen = Screen()
screen.screensize(800,600)
screen.bgcolor("black")

right_paddle = Paddle()
right_paddle.create_paddle(350, 0)
left_paddle = Paddle()
left_paddle.create_paddle(-350, 0)
ball = Ball()

screen.onkey(left_paddle.move_up, "Up")
screen.onkey(left_paddle.move_down, "Down")
screen.listen()

while game_is_on:
    right_paddle.automated_movement()

                           
screen.exitonclick()