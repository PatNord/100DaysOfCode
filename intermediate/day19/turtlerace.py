import turtle
import random

screen = turtle.Screen()
screen.setup(500, 400)
colors = ["red", "green", "yellow", "blue", "orange", "violet"]
y_positions = [-100, -50, 0, 50, 100, 150]

user_bet = screen.textinput(title="make your bet", prompt= "which turtle will win the race? Pick your color!")

turtles = []

for i in range(0, 6):
    new_turtle = turtle.Turtle("turtle")
    new_turtle.up()
    new_turtle.color(colors[i])
    new_turtle.goto(-240, y_positions[i])
    new_turtle.name = colors[i] + "_turtle"
    turtles.append(new_turtle)


finish_line = 240
race_is_on = True

while race_is_on:
    random_turtle = turtles[random.randint(0, 5)]
    random_turtle.forward(random.randint(1, 15))

    if random_turtle.xcor() >= finish_line:
        winning_color = random_turtle.pencolor()
        print(f"Winner is {winning_color}")
        race_is_on = False
        if user_bet == winning_color:
            print("User bet is correct!")
        else:
            print("Player lost!")




screen.exitonclick()