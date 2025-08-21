import turtle

class Snake:
    def __init__(self):
        self.segments = []
        self.make_starting_segments()
        self.head = self.segments[0]
        self.direction_changed = False
    
    def make_starting_segments(self):
        x_starting_positions = [0, -25, -50]
        for i in range(3):
            new_turtle = turtle.Turtle(shape="square")
            new_turtle.color("white")
            new_turtle.penup()
            new_turtle.goto(x_starting_positions[i], 0)
            self.segments.append(new_turtle)
    
    def add_tail(self):
        new_turtle = turtle.Turtle(shape="square")
        new_turtle.color("white")
        new_turtle.penup()
        last_segment = self.segments[-1]
        new_turtle.goto(last_segment.xcor(), last_segment.ycor())
        self.segments.append(new_turtle)

    def move(self):
        for seg_num in range(len(self.segments) -1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.segments[0].forward(25)
        self.direction_changed = False
    

    
    def up(self):
        if self.segments[0].heading() != 270 and not self.direction_changed:
            head = self.segments[0]
            head.setheading(90)
            self.direction_changed = True
    def down(self):
        if self.segments[0].heading() != 90 and not self.direction_changed:
            head = self.segments[0]
            head.setheading(270)
            self.direction_changed = True
    def left(self):
        if self.segments[0].heading() != 0 and not self.direction_changed:
            head = self.segments[0]
            head.setheading(180)
            self.direction_changed = True
    def right(self):
        if self.segments[0].heading() != 180 and not self.direction_changed:
            head = self.segments[0]
            head.setheading(0)
            self.direction_changed = True