from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.title("Pong Game")
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.tracer(0)  # Controla la animación

# Paddle
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

game_is_on = True

while game_is_on:
    screen.update()  # Recien se actualiza

screen.exitonclick()

