import turtle as t

tim = t.Turtle()
tim.shape("turtle")
tim.color("blue")


def calculate_interior_angle(number_of_sides: int):
    return 180*(number_of_sides - 2) / number_of_sides


screen = t.Screen()
screen.exitonclick()

