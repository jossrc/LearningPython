from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "orange", "pink", "green", "blue", "purple"]
racers: dict[str, Turtle] = {}


def get_ready(starting_colors: list[str]):
    y = -100
    for color in starting_colors:
        racers[color] = Turtle(shape="turtle")
        racers[color].color(color)
        racers[color].penup()
        racers[color].goto(-230, y)
        y += 40


get_ready(colors)

screen.exitonclick()
