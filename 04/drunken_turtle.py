import turtle
import random

drunken_level = 10


def drunken_move():
    turtle.setheading(random.randint(0,360))
    turtle.forward(random.randint(100, 200))
    turtle.stamp()

turtle.shape('turtle')

while (1):
    turtle.setheading(random.randint(0,360))
    turtle.forward(random.randint(100, 200))
    turtle.stamp()

