from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

colors = ["red", "orange", "pink", "green", "blue", "purple"]
racers: dict[str, Turtle] = {}
is_race_on = False

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)

if user_bet:
    is_race_on = True

x = -230
y = -100
for color in colors:
    racers[color] = Turtle(shape="turtle")
    racers[color].color(color)
    racers[color].penup()
    racers[color].goto(x, y)
    y += 40

while is_race_on:
    for turtle in racers.values():
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! the {winning_color} turtle is the winner!")
            break
        rand_distance = random.randint(1, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
