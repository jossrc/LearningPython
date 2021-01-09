from turtle import Turtle, Screen

timmy = Turtle()

timmy.shape("turtle")
timmy.color("red")


# Draw a Square

def move_turtle(turtle: Turtle, angle: float, steps: int):
    turtle.forward(steps)
    turtle.right(angle)


SIDES_OF_A_SQUARE = 4


for _ in range(SIDES_OF_A_SQUARE):
    move_turtle(timmy, 90, 100)

screen = Screen()
screen.exitonclick()
