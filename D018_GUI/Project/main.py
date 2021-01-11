import colorgram
import random
import turtle as t


def extract_colors_from(img: str, count: int):
    rgb_colors: list[tuple[int, int, int]] = []
    colors = colorgram.extract(img, count)
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        rgb_colors.append((r, g, b))
    return rgb_colors


rgb_color_list = extract_colors_from('image.jpg', 30)


def draw_dotted_line(turtle: t.Turtle, space: float, steps: int):
    for _ in range(steps):
        turtle.dot(20, random.choice(rgb_color_list))
        turtle.penup()
        turtle.forward(space)


def draw_dotted_square(turtle: t.Turtle, space: float, number_of_points_per_side: int):
    for _ in range(number_of_points_per_side):
        draw_dotted_line(turtle, space, number_of_points_per_side)
        turtle.backward(space*number_of_points_per_side)
        turtle.left(90)
        turtle.forward(space)
        turtle.right(90)


t.colormode(255)
timmy = t.Turtle()
timmy.hideturtle()
timmy.speed("fastest")

draw_dotted_square(timmy, 30, 10)

screen = t.Screen()
screen.exitonclick()
