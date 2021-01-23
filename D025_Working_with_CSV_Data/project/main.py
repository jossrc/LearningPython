import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
data_state = data["state"]
list_of_states = data_state.tolist()
count_of_states = len(list_of_states)


def print_text(message, cx, cy, size):
    text = turtle.Turtle()
    text.hideturtle()
    text.penup()
    text.goto(cx, cy)
    text.write(message, align="center", font=("Courier", size, "normal"), )


score = 0
end_of_game = False

while not end_of_game:

    if score > count_of_states:
        end_of_game = True
        break

    answer_state = screen.textinput(
        title=f"{score}/{count_of_states} States Correct",
        prompt="What's another state's name?"
    ).title()

    if answer_state in list_of_states:
        state = data[data_state == answer_state]
        x = float(state.x)
        y = float(state.y)

        print_text(answer_state, x, y, 12)

        list_of_states.remove(answer_state)
        score += 1
    else:
        print_text(f"GAME OVER - Your score : {score}/{count_of_states}", 0, 0, 24)
        end_of_game = True

screen.exitonclick()
