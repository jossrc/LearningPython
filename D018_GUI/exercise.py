import turtle as t

tim = t.Turtle()
tim.shape("turtle")
tim.color("blue")


def calculate_exterior_angle(number_of_sides: int):
    return 360/number_of_sides


def move_turtle(turtle: t.Turtle, steps: int, angle: float):
    turtle.forward(steps)
    turtle.right(angle)


def draw_polygon(turtle, number_of_sides):
    for _ in range(number_of_sides):
        angle_of_polygon = calculate_exterior_angle(number_of_sides)
        move_turtle(turtle, 100, angle_of_polygon)


# Draw polygons (3 - 10)

for polygon in range(3, 11):
    draw_polygon(tim, polygon)

screen = t.Screen()
screen.exitonclick()

