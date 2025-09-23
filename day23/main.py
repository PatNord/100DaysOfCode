from turtle import Turtle, Screen
import random
from playerturtle import Playerturtle
from car import Car
from scoreboard import Scoreboard
import time

game_is_on = True

screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=800)

turtle = Playerturtle()
score = Scoreboard()

screen.listen()
screen.onkey(turtle.move_up, "Up")
screen.onkey(turtle.move_down, "Down")
screen.onkey(turtle.move_left, "Left")
screen.onkey(turtle.move_right, "Right")

cars = []
car_spawn_counter = 0
car_spawn_rate = 15

def collision_check(turtle, cars):
    for car in cars:
        if turtle.distance(car) < 20:
            return True
    return False

while game_is_on:
    time.sleep(0.05) 
    screen.update()
    car_spawn_counter += 1
    if car_spawn_counter >= car_spawn_rate:
        nc = Car()
        cars.append(nc)
        car_spawn_counter = 0
    cars_to_remove = []
    for car in cars:
        if car.xcor() < -400:
            car.hideturtle()
            cars_to_remove.append(car)
        else:
            car.move()
        
    for car in cars_to_remove:
        cars.remove(car)

    if collision_check(turtle, cars):
        print("Hävisit pelin!")
        game_is_on = False
    
    if turtle.ycor() >= 380:
        turtle.reset_position()
        Car.increase_difficulty()
        score.point()



screen.exitonclick()