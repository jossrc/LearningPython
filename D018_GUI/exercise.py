import turtle as t

tim = t.Turtle()
tim.shape("turtle")
tim.color("blue")


def calculate_interior_angle(number_of_sides: int):
    return 180*(number_of_sides - 2) / number_of_sides


def move_turtle(turtle: t.Turtle, steps: int, angle: float):
    turtle.forward(steps)
    turtle.right(angle)


def draw_polygon(turtle, number_of_sides):
    for _ in range(number_of_sides):
        angle_of_polygon = calculate_interior_angle(number_of_sides)
        move_turtle(turtle, 200, angle_of_polygon)


draw_polygon(tim, 6)

screen = t.Screen()
screen.exitonclick()

