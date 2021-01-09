import turtle as t

timmy = t.Turtle()

timmy.shape("turtle")
timmy.color("red")


# Move turtle

def move_turtle(turtle, angle, steps):
    turtle.forward(steps)
    turtle.right(angle)


# Draw a dashed line

def draw_dashed_line(turtle, steps):
    for _ in range(steps):
        turtle.dot()
        turtle.penup()
        turtle.forward(steps)


SIDES_OF_A_SQUARE = 4

for _ in range(SIDES_OF_A_SQUARE):
    move_turtle(timmy, 90, 100)

timmy.left(90)

draw_dashed_line(timmy, 10)

screen = t.Screen()
screen.exitonclick()
