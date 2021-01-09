import turtle as t
import random

tim = t.Turtle()
tim.shape("turtle")
tim.color("blue")

directions = [tim.forward, tim.backward, tim.right, tim.left]

while True:
    steps = random.randint(10, 30)
    move = random.choice(directions)
    angle = random.randint(1, 3) * 90

    if move == tim.forward or move == tim.backward:
         move(steps)
    else:
        move(angle)
