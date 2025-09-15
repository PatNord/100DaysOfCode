from turtle import Turtle, Screen
from paddle import Paddle

screen = Screen()
screen.screensize(800,600)
screen.bgcolor("black")

right_paddle = Paddle()
right_paddle.create_paddle(350, 0)
left_paddle = Paddle()
left_paddle.create_paddle(-350, 0)
    
screen.onkey(left_paddle.move_up, "Up")
screen.onkey(left_paddle.move_down, "Down")
screen.listen()
screen.exitonclick()