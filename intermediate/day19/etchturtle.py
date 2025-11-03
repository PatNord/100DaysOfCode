import turtle


kilppari = turtle.Turtle()
kilppari.shape("turtle")

def move_forward():
    kilppari.forward(10)
def move_backward():
    kilppari.backward(10)
def counter_clockwise():
    kilppari.left(10)
def clockwise():
    kilppari.right(10)
def clear_screen():
    screen.reset()
    


screen = turtle.Screen()
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()
