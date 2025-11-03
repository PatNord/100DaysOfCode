import turtle 
import random

hirst_colors = [(233, 233, 232), (231, 233, 237), (236, 231, 234), (222, 232, 226), (208, 160, 82), (54, 89, 131), (146, 91, 40), (140, 26, 48), (222, 206, 108), 
                (132, 177, 203), (158, 45, 83), (47, 55, 103), (167, 160, 38), (128, 189, 143), (84, 20, 44), (36, 42, 70), (187, 93, 105), (187, 139, 170), (84, 123, 181), 
                (59, 39, 31), (78, 153, 165), (88, 157, 91), (195, 79, 72), (45, 74, 78), (161, 202, 220), (80, 73, 44), (57, 131, 121), (218, 176, 188), (220, 183, 166), (166, 207, 165)]

kilppari = turtle.Turtle()
kilppari.shape("turtle")
turtle.colormode(255)

def random_color():
    color = []
    for i in range(3):
        x = random.randint(0,255)
        color.append(x)
    return tuple(color)

def triangle():
    kilppari.color(random_color())
    for i in range(3):
        kilppari.forward(100)
        kilppari.right(120)
def square():
    kilppari.color(random_color())
    for i in range(4):
        kilppari.forward(100)
        kilppari.right(90)
def pentagon():
    kilppari.color(random_color())
    for i in range(5):
        kilppari.forward(100)
        kilppari.right(72)
def hexagon():
    kilppari.color(random_color())
    for i in range(6):
        kilppari.forward(100)
        kilppari.right(60)
def heptagon():
    kilppari.color(random_color())
    for i in range(7):
        kilppari.forward(100)
        kilppari.right(51.43)
def octagon():
    kilppari.color(random_color())
    for i in range(8):
        kilppari.forward(100)
        kilppari.right(45)
def nonagon():
    kilppari.color(random_color())
    for i in range(9):
        kilppari.forward(100)
        kilppari.right(40)
def decagon():
    kilppari.color(random_color())
    for i in range(10):
        kilppari.forward(100)
        kilppari.right(36)

def random_walk():
    orientations = [0, 90, 180, 270]
    kilppari.speed(0)
    kilppari.pensize(10)

    for i in range(500):
        kilppari.color(random_color())
        kilppari.forward(25)
        kilppari.seth(random.choice(orientations))

def spirograph():
    degree = 0
    kilppari.speed(0)
    while degree < 360:
        kilppari.color(random_color())
        kilppari.circle(100)
        degree += 5
        kilppari.seth(degree)

def make_hirst():
    kilppari.up()
    x = -250
    y = -250
    for _ in range(10):
        kilppari.goto(x, y)
        for i in range(10):
            kilppari.dot(20, random.choice(hirst_colors))
            kilppari.fd(50)
            y += 5

make_hirst()






screen = turtle.Screen()
screen.exitonclick()