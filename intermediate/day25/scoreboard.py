from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(0, 260)
        self.display_score()

    def update_scoreboard(self):
        self.score += 1
        self.display_score()
    
    def display_score(self):
        self.clear()  # Clear previous score
        self.write(f"{self.score}/50", align="center", font=("Arial", 16, "normal"))

    def create_state_label(self, state_name, x_coord, y_coord):
        state_turtle = Turtle()
        state_turtle.hideturtle() 
        state_turtle.penup()
        state_turtle.goto(x_coord, y_coord)
        state_turtle.write(state_name.title(), align="center", font=("Arial", 8, "normal"))