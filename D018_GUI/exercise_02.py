import turtle as t
import random

tim = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


tim.shape("turtle")
tim.pensize(15)
# tim.speed("fastest")

while True:
    tim.color(random_color())
    steps = 30
    angle = random.randint(0, 3) * 90

    tim.forward(steps)
    tim.setheading(angle)
